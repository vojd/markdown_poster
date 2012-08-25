from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from filebrowser.fields import FileBrowseField
from markdown_proj.apps.blog.models import Blog, Page


class MarkdownDocument(models.Model):

    ALLOWED_MARKDOWN_EXTENSIONS = ['.md', ]

    document = FileBrowseField(verbose_name=_('document'), max_length='255',
        null=True, blank=True,
        extensions=ALLOWED_MARKDOWN_EXTENSIONS)

    def __unicode__(self):
       return u'%s' % self.document

    def save(self, force_insert=False, force_update=False, using=None):
        print 'saving MarkdownDocument'
        super(MarkdownDocument, self).save(force_insert, force_update, using)


class MarkdownDocumentHandler(object):

    # TODO: Check that instance is a valid .md-document

    def __init__(self, document):
        print type(document)
        #assert type(instance) == str

        self.delimiter = '::'
        self.document = document
        # holds the final meta data
        self.meta = {}

    def pre_parse(self):
        """ Read the first lines of the document for meta data """
        file = open(self.document)
        prev_line = None
        for line in file.readlines():
            # Check for meta statements
            if line.startswith(self.delimiter):
                self.update_meta(line)

            else:
                # Check for a title
                # A H1 block is set either by # at the start of the line
                # or by === under the line
                if not self.meta.get('title'):
                    self.get_and_set_title(line, prev_line)
                prev_line = line
        # we're finished and all meta data is stored in self.meta
        print self.meta

    def update_meta(self, line):
        """ Expects a line starting with ``::`` """
        # remove the two first colons, and split the line in two
        try:
            key, value = line[2:].split(':')
        except Exception as e:
            key, value = None, None
        if key and value:
            self.meta.update({key.strip() : value.strip()})

    def get_and_set_title(self, line, prev_line=None):
        """ Check if this line is a title
            if the title isn't set, then we can safely search for it
            Start with checking for regular pound title
            After that search for '===' created headlines
        """

        # we need to trim the line before testing
        line = line.strip()
        if line.startswith('#') and line[2] is not "#":
            self.set_title(line)

        # now check for a row completely made up from '==' chars
        elif "=" * len(line) == line:
            self.set_title(prev_line)

    def set_title(self, title):
        """ Sets the title for this page """
        # strip newline
        if title and title.endswith('\n'):
            title = title[:-1]
        self.meta.update({'title' : title})

    def save(self):
        # TODO: Move these to settings file
        # Possible types mapped between meta name and Model class
        TYPES = {'blog' : Blog, 'page' : Page}

        # run through the meta and set values accordingly
        if hasattr(self.meta, 'created'):
            self.meta['created'] = lambda n : n
        # checking that self.meta isn't empty
        if self.meta:
            # TODO: Create title from Slug or from first H1
            TYPES[self.meta.get('type')].objects.create(
                slug    = self.meta.get('slug', ''),
                title   = self.meta.get('title', ''),
                created = self.meta.get('created', '')
            )

    def run(self):
        """ Main method, runs the pre parsing """

        if not self.document:
            raise Exception
        self.pre_parse()
        self.save()



@receiver(post_save, sender=MarkdownDocument)
def markdown_callback(sender, **kwargs):
    """ WHen a MarkdownDocument is saved this method gets to work """
    instance = kwargs.get('instance')
    md = MarkdownDocumentHandler(instance.document)
    md.run()

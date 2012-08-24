from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from filebrowser.fields import FileBrowseField


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
        for line in file.readlines():
            if line.startswith(self.delimiter):
                self.dispatch_action(line)
        # we're finished and all meta data is stored in self.meta
        print self.meta

    def dispatch_action(self, line):
        """ Expects a line starting with ``::`` """
        # remove the two first colons, and split the line in two
        key, value = line[2:].split(':')
        print key, value
        self.meta.update({key : value})

    def run(self):
        """ Main method, runs the pre parsing """
        print dir(self.document)
        import pdb
        pdb.set_trace()

        #if not self.instance:
        #    raise Exception
        #self.pre_parse()



@receiver(post_save, sender=MarkdownDocument)
def markdown_callback(sender, **kwargs):
    """ WHen a MarkdownDocument is saved this method gets to work """
    instance = kwargs.get('instance')
    md = MarkdownDocumentHandler(instance.document)
    md.run()

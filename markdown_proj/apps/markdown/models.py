from django.db import models
from django.utils.translation import ugettext as _
from filebrowser.fields import FileBrowseField

class MarkdownDocument(models.Model):

    document = FileBrowseField(max_length=255, verbose_name=_('document'))

    def __unicode__(self):
       return u'%s' % self.document



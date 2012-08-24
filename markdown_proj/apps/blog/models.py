from django.db import models

class Displayable(models.Model):
    """ Base class for our simple blog """
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.slug

    class Meta:
        abstract = True

class Blog(Displayable):
    pass

class Page(Displayable):
    pass
# signals for the markdown handler / parser
# when a markdown document is saved we'll
# notify the handler to get to work

# TODO: the parser/handler could be built as a Celery task

from django.db.models.signals import post_save
from django.dispatch import receiver
from markdown_proj.apps.markdown.models import MarkdownDocument

@receiver(post_save, sender=MarkdownDocument)
def markdown_callback(sender, **kwargs):
    """ WHen a MarkdownDocument is saved this method gets to work """
    print "markdown handler is off to work!"

def markdown_handler(sender, **kwargs):
    print 'markdown_handler sender', sender
    print kwargs




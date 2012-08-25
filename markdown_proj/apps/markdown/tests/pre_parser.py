import os
from django.utils.unittest.case import TestCase
from markdown_proj.apps.markdown.models import MarkdownDocument, MarkdownDocumentHandler

class MarkdownTestCase(TestCase):

    def setUp(self):
        print 'starting MarkdownTestCase'

    def tearDown(self):
        print 'tearing down MarkdownTestCase'

    def test_save_signal(self):
        """ Tests that save signal works as intended """

        # create a MarkdownDocument object
        # this implicitly saves the object and shall invoke the signal dispatcher
        # in models.py
        from django.conf import settings
        md = MarkdownDocument.objects.create(
            document=os.path.abspath('test_markdown.md'))

        # TODO: Do the actual test ;)

    def test_document_handler(self):
        """ Test the MarkdownDocumentHandler class functionality """


        document = os.path.join(os.path.dirname(__file__), 'test_markdown.md')
        md = MarkdownDocumentHandler(document)
        md.run()

        self.assertTrue(md.meta.get('slug'))
        #blog = Blog.objects.get(slug=md.meta.get('slug'))





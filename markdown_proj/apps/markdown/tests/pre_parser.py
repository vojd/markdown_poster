import os
from django.utils.unittest.case import TestCase
from markdown_proj.apps.markdown.models import MarkdownDocument

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
        




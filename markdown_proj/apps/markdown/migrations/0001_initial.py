# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MarkdownDocument'
        db.create_table('markdown_markdowndocument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('filebrowser.fields.FileBrowseField')(max_length=255)),
        ))
        db.send_create_signal('markdown', ['MarkdownDocument'])


    def backwards(self, orm):
        # Deleting model 'MarkdownDocument'
        db.delete_table('markdown_markdowndocument')


    models = {
        'markdown.markdowndocument': {
            'Meta': {'object_name': 'MarkdownDocument'},
            'document': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['markdown']
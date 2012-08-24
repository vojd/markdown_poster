# Django settings for markdown_proj project.

import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db/database.sqlite',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

PROJECT_ROOT        = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
STATIC_ROOT         = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL          = '/static/'
STATIC_THEME_URL    = os.path.join(STATIC_URL, 'shirtstheme')
MEDIA_ROOT          = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL           = '/media/'
FILEBROWSER_MEDIA_URL = MEDIA_ROOT
EXTENSIONS = \
    {'Folder': [''],
     'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv', '.md'],
     'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
     'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
     'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']}

# Additional locations of static files
STATICFILES_DIRS = (
    '/static',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b9#jzfbhtm03br!z50rwvuon*^2+doz%g7fksu5yov12=-aqg3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'markdown_proj.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'markdown_proj.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'south',

    'markdown_proj.apps.markdown',
    'markdown_proj.apps.blog',


)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

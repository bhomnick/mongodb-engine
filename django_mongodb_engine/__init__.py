#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__ = (0, 4, 0)
__author__ = "Flavio Percoco Premoli, Alberto Paro, " + \
             "Jonas Haag and contributors"
__contact__ = "django-non-relational@googlegroups.com"
__homepage__ = "https://django-mongodb.org"
__docformat__ = "restructuredtext"

try:
    from django.conf import settings
    settings.INSTALLED_APPS.insert(0, 'django_mongodb_engine')
    # It might be irritating that django-mongodb-engine registers itself as an app,
    # and I think this is worth an explanation - so here you go:
    # django-mongodb-engine provides a way to set MongoDB-specific options for a
    # certain model via the 'MongoMeta' class/attribute (similar to the Django-style
    # 'Meta' class).  We want those options to be copied into the model's
    # '_meta' object, right after the class has been defined.
    # For this, we have to listen to the 'class_prepared' signal from
    # 'django.db.models.signals'. Because the 'django_mongodb_engine' module gets
    # imported as part of the initialization process of Django's ORM ('django.db'),
    # we can *not* import anything from 'django.db' in this file (or any other
    # submodule that is imported during the ORM initialization) because that would
    # get us into recursive import hell which the Python interpreter doesn't allow.
    # The only way to make sure certain code is executed after Django's ORM has been
    # initialized is registering an app. After initializing itself, Django imports
    # all apps defined in the project's 'settings.py' in the order implied by
    # iterating over the INSTALLED_APPS list. As we have to make sure that
    # django-mongodb-engine is loaded very first, we prepend it to the list.
except ImportError:
    pass

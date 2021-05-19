# copy this as `local.py` into the `djBackend` folder if on the server system
SERVER_ENV = True

DEBUG = False

ALLOWED_HOSTS = ["<IP ADD>", "localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<DB Name>',
        'USER': '<User name>',
        'PASSWORD': '<PWD>',
        'HOST': '<IP ADD>',
        'PORT': 5432,
    }}



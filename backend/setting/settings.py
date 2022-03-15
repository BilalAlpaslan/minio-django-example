from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'wd3(+*ybu+5_q-h$@3e9dz+$^*3d=^%ee!wvegwv1#*nugv1dl'

DEBUG = True 

ALLOWED_HOSTS = ["*"]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # -------------------------------------------------
    'storages',
    'rest_framework',
    'corsheaders',
    # --------------------------------------------------
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'setting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setting.wsgi.application'

DATABASES = {
    # sqlite connection
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_S3 = True

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID =  "minio"
    AWS_SECRET_ACCESS_KEY = "minio123"

    AWS_STORAGE_BUCKET_NAME = "example"
    AWS_S3_ENDPOINT_URL = "http://localhost:9000"

    AWS_DEFAULT_ACL = None
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'setting.storage.StaticStorage'

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'setting.storage.PublicMediaStorage'

    # s3 private media settings
    # PRIVATE_MEDIA_LOCATION = 'private'
    # PRIVATE_FILE_STORAGE = 'hello_django.storage_backends.PrivateMediaStorage'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)



REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 4,
    'DEFAULT_AUTHENTICATION_CLASSES':('knox.auth.TokenAuthentication',),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

CORS_ORIGIN_ALLOW_ALL = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_KNOX = {'TOKEN_TTL': None}

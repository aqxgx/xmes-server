"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

try:
    from config import *
except ImportError:
    print("未发现自定义配置，使用默认配置")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = locals().get("SECRET_KEY", 'django-insecure-mlq6(#a^2vk!1=7=xhp#$i=o5d%namfs=+b26$m#sh_2rco7j^')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = locals().get("DEBUG", False)
LOG_LEVEL = locals().get('LOG_LEVEL', "DEBUG")
DEBUG_DEV = locals().get('DEBUG_DEV', False)

# 如果前端是代理，则可以通过该配置，在系统构建url的时候，获取正确的 scheme
# 需要在 前端加入该配置  proxy_set_header X-Forwarded-Proto $scheme;
# https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#std-setting-SECURE_PROXY_SSL_HEADER
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# 为了兼容前端NGINX代理，并且使用非80，443端口访问，详细查看源码：django.http.request.HttpRequest._get_raw_host
# https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#use-x-forwarded-host
USE_X_FORWARDED_HOST = True

ALLOWED_HOSTS = locals().get("ALLOWED_HOSTS", ["*"])

# Application definition
XADMIN_APPS = locals().get("XADMIN_APPS", [])

# 表前缀设置
# 1.指定配置
# DB_PREFIX={
# 'system': 'abc_', # system app所有的表都加前缀 abc_
# 'system.config':'xxa_', # 仅system.config添加前缀 xxa_
# '': '', # 默认前缀
# }
#
# 2.全局配置
# DB_PREFIX='abc_'  : 所有表都添加 abc_
DB_PREFIX = locals().get("DB_PREFIX", "")

INSTALLED_APPS = [
    'daphne',  # 支持websocket
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'system.apps.SystemConfig',  # 系统管理
    'settings.apps.SettingsConfig',  # 设置相关
    "notifications.apps.NotificationsConfig",  # 消息通知相关
    'captcha.apps.CaptchaConfig',  # 图片验证码
    'message.apps.MessageConfig',  # websocket 消息
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'django_celery_results',
    'django_celery_beat',
    'imagekit',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    *XADMIN_APPS,
    'common.apps.CommonConfig',  # 这个放到最后, django ready
]

MIDDLEWARE = [
    'server.middleware.StartMiddleware',
    'server.middleware.RequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'server.middleware.RefererCheckMiddleware',
    'server.middleware.SQLCountMiddleware',
    'common.core.middleware.ApiLoggingMiddleware',
    'server.middleware.EndMiddleware'
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

# WSGI_APPLICATION = 'server.wsgi.application'
ASGI_APPLICATION = "server.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Redis 配置
REDIS_HOST = locals().get("REDIS_HOST", "redis")
REDIS_PORT = locals().get("REDIS_PORT", 6379)
REDIS_PASSWORD = locals().get("REDIS_PASSWORD", "nineven")

DEFAULT_CACHE_ID = 1
CHANNEL_LAYERS_CACHE_ID = 2
CELERY_BROKER_CACHE_ID = 3
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{DEFAULT_CACHE_ID}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 8000},
            "PASSWORD": REDIS_PASSWORD,
            "DECODE_RESPONSES": True
        },
        "TIMEOUT": 60 * 15,
        "KEY_FUNCTION": "common.base.utils.redis_key_func",
        "REVERSE_KEY_FUNCTION": "common.base.utils.redis_reverse_key_func",
    },
}

# create database xadmin default character set utf8 COLLATE utf8_general_ci;
# grant all on xadmin.* to server@'127.0.0.1' identified by 'KGzKjZpWBp4R4RSa';
# python manage.py makemigrations
# python manage.py migrate
DATABASES = {
    'default': {
        'ENGINE': locals().get('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': locals().get('DB_DATABASE', BASE_DIR / "db.sqlite3"),
        'HOST': locals().get('DB_HOST', 'mariadb'),
        'PORT': locals().get('DB_PORT', 3306),
        'USER': locals().get('DB_USER', 'server'),
        'PASSWORD': locals().get('DB_PASSWORD', 'KGzKjZpWBp4R4RSa'),
        'CONN_MAX_AGE': 600,
        # 设置MySQL的驱动
        # 'OPTIONS': {'init_command': 'SET storage_engine=INNODB'},
        # 'OPTIONS': {'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"', 'charset': 'utf8mb4'},
        'OPTIONS': locals().get('OPTIONS', {}),
    }
}
# https://docs.djangoproject.com/zh-hans/5.0/topics/db/multi-db/#automatic-database-routing
# 读写分离 可能会出现 the current database router prevents this relation.
# 1.项目设置了router读写分离，且在ORM create()方法中，使用了前边filter()方法得到的数据，
# 2.由于django是惰性查询，前边的filter()并没有立即查询，而是在create()中引用了filter()的数据时，执行了filter()，
# 3.此时写操作的db指针指向write_db，filter()的db指针指向read_db，两者发生冲突，导致服务禁止了此次与mysql的交互
# 解决办法：
# 在前边filter()方法中，使用using()方法，使filter()方法立即与数据库交互，查出数据。
# Author.objects.using("default")
# >>> p = Person(name="Fred")
# >>> p.save(using="second")  # (statement 2)

DATABASE_ROUTERS = ['common.core.db.router.DBRouter']

# websocket 消息需要用到redis的消息发布订阅
CHANNEL_LAYERS = {
    "default": {
        # "BACKEND": "channels_redis.core.RedisChannelLayer",
        "BACKEND": "channels_redis.pubsub.RedisPubSubChannelLayer",
        "CONFIG": {
            "hosts": [f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{CHANNEL_LAYERS_CACHE_ID}"],
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
# http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = "system.UserInfo"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'api/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# STATICFILES_FINDERS = (
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder"
# )
# 收集静态文件
# python manage.py collectstatic


# Media配置
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "upload")
FILE_UPLOAD_SIZE = 1024 * 1024 * 10  # 文件上传大小限制,默认10兆
PICTURE_UPLOAD_SIZE = 1024 * 1024 * 0.5  # 头像图片上传大小，默认为500kb
FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'common.swagger.utils.CustomAutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        # 'common.drf.renders.CSVFileRenderer', # 为什么注释：因为导入导出需要权限判断，在导入导出功能中再次自定义解析数据
        # 'common.drf.renders.ExcelFileRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'common.drf.parsers.AxiosMultiPartParser',
        'common.drf.parsers.CSVFileParser',
        'common.drf.parsers.ExcelFileParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'common.core.auth.CookieJWTAuthentication',
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",  # 允许basic授权，方便调试使用
    ],
    'EXCEPTION_HANDLER': 'common.core.exception.common_exception_handler',
    'DEFAULT_METADATA_CLASS': 'common.drf.metadata.SimpleMetadataWithFilters',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {  # {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        'anon': '60/m',
        'user': '600/m',
        'upload': '100/m',
        'download1': '10/m',
        'download2': '100/h',
        'register': '50/d',
        'reset_password': '50/d',
        'login': '50/h',
        **locals().get('DEFAULT_THROTTLE_RATES', {})
    },
    'DEFAULT_PAGINATION_CLASS': 'common.core.pagination.PageNumber',
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        'common.core.permission.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'common.core.filter.BaseDataPermissionFilter',
    ),
}

# DRF扩展缓存时间
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 3600,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=3600),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=15),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,  # 在登录的时候更新user表  last_login 字段

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': 'x',
    'ISSUER': 'server',
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('common.core.auth.ServerAccessToken',),
    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'POST',
    'PUT',
    'PATCH',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "x-token"
)

# I18N translation
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

CACHE_KEY_TEMPLATE = {
    'config_key': 'config',
    'make_token_key': 'make_token',
    'download_url_key': 'download_url',
    'pending_state_key': 'pending_state',
    'user_websocket_key': 'user_websocket',
    'upload_part_info_key': 'upload_part_info',
    'black_access_token_key': 'black_access_token',
    'common_resource_ids_key': 'common_resource_ids',
    **locals().get('CACHE_KEY_TEMPLATE', {})
}

# Celery Configuration Options
# https://docs.celeryq.dev/en/stable/userguide/configuration.html?
CELERY_TIMEZONE = "Asia/Shanghai"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

# CELERY_RESULT_BACKEND = ''
# CELERY_CACHE_BACKEND = 'django-cache'

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'default'

# broker redis
DJANGO_DEFAULT_CACHES = CACHES['default']
CELERY_BROKER_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{CELERY_BROKER_CACHE_ID}'

# CELERY_WORKER_CONCURRENCY = 10  # worker并发数
CELERY_WORKER_AUTOSCALE = [10, 3]  # which needs two numbers: the maximum and minimum number of pool processes

CELERYD_FORCE_EXECV = True  # 非常重要,有些情况下可以防止死
CELERY_RESULT_EXPIRES = 3600 * 24 * 7  # 任务结果过期时间

CELERY_WORKER_DISABLE_RATE_LIMITS = True  # 任务发出后，经过一段时间还未收到acknowledge , 就将任务重新交给其他worker执行
CELERY_WORKER_PREFETCH_MULTIPLIER = 60  # celery worker 每次去redis取任务的数量

CELERY_WORKER_MAX_TASKS_PER_CHILD = 200  # 每个worker执行了多少任务就会死掉，我建议数量可以大一些，比如200

CELERY_ENABLE_UTC = False
DJANGO_CELERY_BEAT_TZ_AWARE = True

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# celery消息的序列化方式，由于要把对象当做参数所以使用pickle
# CELERY_RESULT_SERIALIZER = 'pickle'
# CELERY_ACCEPT_CONTENT = ['pickle']
# CELERY_TASK_SERIALIZER = 'pickle'

APPEND_SLASH = False

HTTP_BIND_HOST = '0.0.0.0'
HTTP_LISTEN_PORT = locals().get('HTTP_LISTEN_PORT', 8896)
GUNICORN_MAX_WORKER = locals().get('GUNICORN_MAX_WORKER', 4)
# celery flower 任务监控配置
CELERY_FLOWER_PORT = 5566
CELERY_FLOWER_HOST = '127.0.0.1'
CELERY_FLOWER_AUTH = 'flower:flower123.'

# 访问白名单配置，无需权限配置, key为路由，value为列表，对应的是请求方式， * 表示全部请求方式, 请求方式为大写
PERMISSION_WHITE_URL = {
    "^/api/system/login$": ['*'],
    "^/api/system/logout$": ['*'],
    "^/api/system/userinfo$": ['GET'],
    "^/api/system/routes$": ['*'],
    "^/api/system/dashboard/": ['*'],
    "^/api/.*choices$": ['*'],
    "^/api/.*search-fields$": ['*'],
    "^/api/common/resources/cache$": ['*'],
    "^/api/notifications/site-messages/unread$": ['*'],
}

# 前端权限路由 忽略配置
ROUTE_IGNORE_URL = [
    "^/api/system/.*choices$",  # 每个方法都有该路由，则忽略即可
    "^/api/.*search-fields$",  # 每个方法都有该路由，则忽略即可
    "^/api/.*search-columns$",  # 该路由使用list权限字段，无需重新配置
    "^/api/settings/.*search-columns$",  # 该路由使用list权限字段，无需重新配置
    "^/api/system/dashboard/",  # 忽略dashboard路由
]

# 访问权限配置
PERMISSION_SHOW_PREFIX = [
    r'api/system',
    r'api/settings',
    r'api/notifications',
    r'api/flower',
    r'api-docs',
]
# 数据权限配置
PERMISSION_DATA_AUTH_APPS = [
    'system',
    'settings',
    'notifications'
]

API_LOG_ENABLE = True
API_LOG_METHODS = ["POST", "DELETE", "PUT", "PATCH"]  # 'ALL'

# 忽略日志记录, 支持model 或者 request_path, 不支持正则
API_LOG_IGNORE = {
    'system.OperationLog': ['GET'],
    '/api/common/api/health': ['GET'],
}

# 在操作日志中详细记录的请求模块映射
API_MODEL_MAP = {
    "/api/system/refresh": "Token刷新",
    "/api/flower": "定时任务",
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Xadmin Server API',
    'DESCRIPTION': 'Django Xadmin Server',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SERVE_PUBLIC': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    "SWAGGER_UI_SETTINGS": {
        "displayRequestDuration": True,
        "deepLinking": True,
        "filter": True,
        "persistAuthorization": True,
        "displayOperationId": False,
    },
    # 'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
}

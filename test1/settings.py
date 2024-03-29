"""
Django settings for test1 project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lr-_)zlcur(p9xy1v7ne6q^-%a-fg#)zq3ctvwb!dy%3!ej*$a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["192.168.137.141"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    "django_filters",
    "rest_framework",


    "books.apps.BooksConfig"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join("templates")],
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

WSGI_APPLICATION = 'test1.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'HOST': "192.168.137.141",
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'books',
        'USER': "root",
        'PASSWORD': 'mysql',
        'PORT': 3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 配置缓存
CACHAS = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.137.141:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 全局配置
REST_FRAMEWORK = {
    # 身份认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "rest_framework.authentication.BasicAuthentication",  # 基本认证
        "rest_framework.authentication.SessionAuthentication"  # session 认证
    ),
    # 权限认证
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',  # 通过身份认证
        # 'rest_framework.permissions.AllowAny',  # 默认 所有权限
        'rest_framework.permissions.IsAdminUser',   # 超级管理员
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',   # 认证用户可以完全操作，未登录只有只读权限
    ),
    # 限流
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',  # 匿名用户
        'rest_framework.throttling.UserRateThrottle'     # 登陆用户
        # 'rest_framework.throttling.ScopedRateThrottle',  # 使用用户名或ip 记录访问次数
    ),
    # 访问次数限制
    'DEFAULT_THROTTLE_RATES': {
        'anon': '200/day',
        'user': '300/day',
        # 'contacts': '200/day',      # 登陆用户记录session_id  非登陆用户记录ip
        # 'uploads': '200/day'
    },
    # drf过滤后端
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # 分页配置
    'DEFAULT_PAGINATION_CLASS':  'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':2 ,  # 每页数目

    # 自定义异常处理函数
    'EXCEPTION_HANDLER': 'books.drf_exceptions.exceptions.drf_exception_handler'
}

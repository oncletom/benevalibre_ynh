import settings

settings.MIDDLEWARE.insert(
    settings.MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
    'benevalibre_ynh.middleware.CustomHeaderMiddleware'
)

settings.AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.RemoteUserBackend'
]

settings.LOGIN_URL = '/yunohost/sso/'

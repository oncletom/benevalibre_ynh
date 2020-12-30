from django.contrib.auth.middleware import PersistentRemoteUserMiddleware

class CustomHeaderMiddleware(PersistentRemoteUserMiddleware):
    """
    Http header added by SSOWat when signed in
    """
    header = 'HTTP_EMAIL'

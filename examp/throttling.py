from rest_framework.throttling import BaseThrottle
from rest_framework.settings import api_settings
import datetime


class ProductUserThrottle(BaseThrottle):
    scope = 'post_user'

    def allow_request(self, request, view):
        date = datetime.datetime.now().time()
        if date != 17 and date != 16:
            return False


class AuthUserThrottle:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response

    def process_request(self, request):
        throttle_classes = api_settings.DEFAULT_THROTTLE_CLASSES
        for throttle in throttle_classes:
            throttle_instance = throttle()
            if throttle_instance.allow_request(request=request, view=None):
                raise "asdsda"

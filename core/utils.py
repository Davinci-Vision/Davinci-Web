from django.shortcuts import render
from davinci_web.settings import *
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = "staticfiles"
    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
        super(StaticStorage, self).__init__(*args, **kwargs)


class MediaStorage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
        super(MediaStorage, self).__init__(*args, **kwargs)


def error_page(request, errormsg=''):
    """Show error page with message"""
    if not errormsg:
        errormsg = "잘못된 접근입니다."

    return render(
        request,
        "error/error.html",
        {
            'errormsg': errormsg,
        }
    )


def error_to_response(request, errormsg=''):
    """Show error response with msg"""
    if not errormsg:
        errormsg = "잘못된 접근입니다."

    return render(
        request,
        "error/error.html",
        {
            'errormsg': errormsg,
        }
    )


def get_ipaddress(request):
    """Return ipaddress"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_referrer(request):
    """Return referrer"""
    referrer = request.META['HTTP_REFERER']
    return referrer


def get_useragent(request):
    """Return useragent"""
    user_agent = request.META['HTTP_USER_AGENT']
    return user_agent


def is_mobile(request):
    """Return true if request from Android and iPhone"""
    user_agent = request.META['HTTP_USER_AGENT']
    if 'Android' in user_agent or 'iPhone' in user_agent:
        return True
    else:
        return False


from django.shortcuts import render
from board.models import *

def index(request):
    lists = Board.objects.filter(status="1normal").order_by('-created_at')[:3]
    return render(request, 'index/index.html', {"lists": lists})

def static_project(request):
    return render(request, 'index/project.html')

def static_tech(request):
    return render(request, 'index/tech.html')

def static_alliance(request):
    return render(request, 'index/alliance.html')

def error_400(request, exception):
    response = render('layout/error.html',{"errormsg":"400 Error - Bad Request"})
    response.status_code = 400
    return response

def error_403(request, exception):
    response = render('layout/error.html', {"errormsg": "403 Error - Permission Denied"})
    response.status_code = 403
    return response

def error_404(request, exception):
    response = render('layout/error.html', {"errormsg": "404 Error - Page Not Founded"})
    response.status_code = 404
    return response

def error_500(request, exception):
    response = render('layout/error.html', {"errormsg": "500 Error - Server Error"})
    response.status_code = 500
    return response

def csrf_failure(request, reason=""):
    ctx = {'errormsg': '세션이 종료되었습니다. 메인 페이지로 이동해주세요.'}
    return render('layout/error.html', ctx)
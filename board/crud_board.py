from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from index.views import *
from django.shortcuts import get_object_or_404, redirect
from core.utils import *
from board.models import *
from .forms import BoardEditForm

@login_required(login_url='/user/signin/')
def new_article(request):
    if not request.user.is_active:
        return redirect('signout')

    if request.method == "POST":
        editform = BoardEditForm(request.POST, request.FILES)

        if editform.is_valid():
            article = editform.save(commit=False)

            if request.FILES:
                article.custom_image = request.FILES['custom_image']
                is_img = article.get_image_text()
                if is_img in article.content:
                    article.has_image = True
                    image_url = article.content.split("src")[1].split('="')[1].split('"')[0]
                    article.main_image = image_url
            else:

                is_img = article.get_image_text()
                if is_img in article.content:
                    article.has_image = True
                    # <img
                    image_url = article.content.split("src")[1].split('="')[1].split('"')[0]
                    article.main_image = image_url
                else:
                    article.has_image = False
                    article.main_image = ""

            article.lang = LangType.objects.get(id=2)
            article.save()

            return redirect(article.get_article_url())
        else:
            editform = BoardEditForm(request.POST)

            return render(
                request,
                'board/edit_article.html',
                {
                    'form': editform,
                    'edit_type': 'new',
                    "msg": "제목/내용/언어 다시 확인해주세요.",
                    "path": "article",
                }
            )
    elif request.method == "GET":

        editform = BoardEditForm()


        return render(
            request,
            'board/edit_article.html',
            {
                'form': editform,
                'edit_type': 'new',
                "path": "media"
            }
        )

    else:
        msg = "해당 요청에 대한 권한이 없습니다."
        return error_403(request, msg)


# Read
def show_article(request, id):

    article = get_object_or_404(Board, pk=id)
    if article.status == '2deleted' and not request.user.is_staff:
        errormsg = "404 NOT FOUND :("
        return error_404(request, errormsg)

    if request.user.is_authenticated:
        is_users = 'true'
    else:
        is_users = 'false'

    return render(request,
                  "board/show_article.html",
                  {
                      'article': article,
                      "is_users": is_users,
                      "path": "article",
                  }
                  )


# Update
@login_required(login_url='/user/signin/')
def edit_article(request, id):
    if not request.user.is_active:
        return redirect('signout')
    """edit article"""
    article = get_object_or_404(Board, pk=id)

    if article.custom_image:
        custom_image = article.custom_image
    else:
        custom_image = ""

    edit_type = 'edit'

    if request.method == "POST":
        editform = BoardEditForm(request.POST, request.FILES, instance=article)
        if editform.is_valid():
            article = editform.save(commit=False)

            if request.FILES:
                article.custom_image = request.FILES['custom_image']
                is_img = article.get_image_text()
                if is_img in article.content:
                    article.has_image = True
                    # <img
                    image_url = article.content.split("src")[1].split('="')[1].split('"')[0]
                    article.main_image = image_url

            else:

                is_img = article.get_image_text()
                if is_img in article.content:
                    article.has_image = True
                    # <img
                    image_url = article.content.split("src")[1].split('="')[1].split('"')[0]
                    article.main_image = image_url
                else:
                    article.has_image = False
                    article.main_image = ""
            article.save()
            return redirect(article.get_article_url())
        else:
            msg = editform.errors

            return render(
                request,
                'board/edit_article.html',
                {
                    'form': editform,
                    'edit_type': edit_type,
                    'created_at': article.created_at,
                    "msg": msg,
                    "path": "article"
                }
            )
    elif request.method == "GET":
        try:
            editform = BoardEditForm(instance=article)
        except:
            return error_404(request)

        return render(
            request,
            'board/edit_article.html',
            {
                'form': editform,
                'edit_type': edit_type,
                'created_at': article.created_at,
                "path": "media",
                "custom_image":custom_image
            }
        )


@login_required(login_url='/user/signin/')
def delete_article(request, id, stay=False):
    if not request.user.is_active:
        return redirect('signout')
    """Delete article"""
    article = get_object_or_404(Board, pk=id)

    if request.user.is_staff:
        article.status = '6deleted'
        article.save()
    else:
        return error_403(request,"")

    return redirect('show_list')


@staff_member_required(login_url='/user/signin/')
def restore_article(request, id):
    if not request.user.is_active:
        return redirect('signout')

    """Restore article"""
    article = get_object_or_404(Board, pk=id)
    if article.status == '6deleted':
        article.status = '1normal'
        article.save()
    else:
        return error_400(request,"")

    return redirect('show_list')
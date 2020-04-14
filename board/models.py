from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

class LangType(models.Model):
    LANG_TYPE = {
        ('1eng', _("english")),
        ('2kr', _('korean')),
        ('3ch', _('china')),
        ('4ja', _('japan')),
    }
    lang_type = models.CharField(
        choices=LANG_TYPE,
        default='1eng',
        verbose_name="게시글 언어",
        help_text="1:영어, 2:한국어, 3:중국어, 4:일본어 | (기본 영어)",
        max_length=20
    )
    def __str__(self):
        return self.lang_type

class Category(models.Model):
    category = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="카테고리"
    )

    def __str__(self):
        return self.category

class Board(models.Model):
    BOARD_STATUS = {
        ('1normal', "오픈"),
        ('6deleted', '숨김'),
    }
    lang = models.ForeignKey(
        LangType,
        on_delete=models.CASCADE,
        verbose_name="언어"
    )
    title = models.CharField(
        max_length=50,
        verbose_name="제목"
    )
    status = models.CharField(
        max_length=20,
        choices=BOARD_STATUS,
        default='1normal',
        verbose_name="게시글 분류",
        help_text="1:공개, 2:임시저장, 3:전체공지, 4:스폰서게시글, 5:숨김, 6:삭제"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="카테고리"
    )

    content = models.TextField(
        verbose_name="내용"
    )

    main_image = models.URLField(
        default='',
        max_length=250,
        blank=True
    )

    custom_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='django-summernote/custom/',
        help_text="커스텀 이미지"
    )

    def __str__(self):
        try:
            if self.status == "1normal":
                return "%s" % (self.title)
            else:
                return "[%s] %s" % ("숨김", self.title)
        except:

            return "[%s] %s" % ("게시판삭제", self.title)

    def get_image_text(self):
        """Get image text"""
        return '<img '

    def get_article_url(self):
        """Back to article"""
        return reverse_lazy('show_article', args=[self.id])
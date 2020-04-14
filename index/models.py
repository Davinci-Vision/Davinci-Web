from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Whitepaper(models.Model):
    LANG_TYPE = {
        ('1eng', _("english")),
        ('2kr', _('korean')),
        ('3ch', _('china')),
        ('4ja', _('japan')),
    }

    lang_type = models.CharField(
        choices=LANG_TYPE,
        default='1eng',
        verbose_name="언어",
        help_text="1:영어, 2:한국어, 3:중국어, 4:일본어",
        max_length=20
    )

    files = models.FileField(
        verbose_name="파일업로드",
        help_text="PDF 파일 업로드",
        upload_to='attach/whitepaper/',
        null=True,
        blank=True
    )

    is_open = models.BooleanField(
        verbose_name="오픈여부",
        default=True,
        help_text="체크박스 시 오픈"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

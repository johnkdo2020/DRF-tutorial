from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    # DB index설정 (feild.DB)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')

    code = models.TextField()

    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        # queryset으로 불러올 때 정렬해서 가져
        # 우리는 created 기준으로 정렬되어있다는 거 알고 있지만
        # django는 모르기 때문에 재정렬 되어 날아온다.
        ordering = ['created']
        # DB index설정 (Model.Meta)
        indexes = [
            models.Index(fields=['created']),
        ]
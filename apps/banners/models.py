from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


class Banner(TimeStampedModel):
    title = models.CharField(_('Asosiy sarlavha'), max_length=128)
    subtitle = models.CharField(_('Kichik sarlavha'), max_length=256)
    picture = models.ImageField(_('Rasm'), upload_to='images/banners/')

    is_active = models.BooleanField(_('Aktivmi?'), default=True)

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Bannerlar')

    def __str__(self):
        return self.title

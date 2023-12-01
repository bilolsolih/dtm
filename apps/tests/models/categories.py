from django.db import models

from django.utils.translation import gettext_lazy as _


class TestCategory(models.Model):
    title = models.CharField(_('Kategoriya nomi'), max_length=256)
    description = models.TextField(_('Kategoriya ta\'rifi'))

    class Meta:
        verbose_name = _('Kategoriya')
        verbose_name_plural = _('Kategoriyalar')

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(_('Fan nomi'), max_length=256, unique=True)

    is_active = models.BooleanField(_('Faollik statusi'), default=True)

    class Meta:
        verbose_name = _('Fan')
        verbose_name_plural = _('Fanlar')
        indexes = [
            models.Index(fields=['title'])
        ]

    def __str__(self):
        return self.title


class Topic(models.Model):
    subject = models.ForeignKey('tests.Subject', related_name='topics', on_delete=models.CASCADE, verbose_name=_('Fan'))
    title = models.CharField(_('Mavzu nomi'), max_length=256)

    class Meta:
        verbose_name = _('Mavzu')
        verbose_name_plural = _('Mavzular')
        unique_together = ['subject', 'title']

    def __str__(self):
        return f'{self.subject} - {self.title}'


__all__ = ['TestCategory', 'Subject', 'Topic']

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


class Attempt(TimeStampedModel):
    student = models.ForeignKey('accounts.User', related_name='attempts', on_delete=models.CASCADE, verbose_name=_('O\'quvchi'))
    subject = models.ForeignKey('tests.Subject', related_name='attempts', on_delete=models.PROTECT, verbose_name=_('Fan'))
    topic = models.ForeignKey('tests.Topic', related_name='attempts', on_delete=models.PROTECT, verbose_name=_('Mavzu'))
    number_of_questions = models.PositiveIntegerField(_('Savollar miqdori'))
    time_limit = models.PositiveIntegerField(_('Vaqti (minut)'))
    result = models.PositiveIntegerField(_('To\'g\'ri javoblar soni'), default=0)

    is_completed = models.BooleanField(_('Yakunlanganmi?'), default=False)

    class Meta:
        verbose_name = _('Urinish')
        verbose_name_plural = _('Urinishlar')

    def __str__(self):
        return f'{self.student.username} - {self.subject} - {self.topic}'


__all__ = ['Attempt']

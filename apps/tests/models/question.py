from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


class Letters(models.TextChoices):
    A = ('A', 'A')
    B = ('B', 'B')
    C = ('C', 'C')
    D = ('D', 'D')


class QuestionType(models.Model):
    title = models.CharField(_('Savol turi'), max_length=128)
    prompt = models.CharField(_('Savol bayoni'), max_length=256)

    class Meta:
        verbose_name = _('Savol turi')
        verbose_name_plural = _('Savol turlari')

    def __str__(self):
        return self.title


class Question(TimeStampedModel):
    subject = models.ForeignKey('tests.Subject', related_name='questions', on_delete=models.PROTECT, verbose_name=_('Fan'))
    topic = models.ForeignKey('tests.Topic', related_name='questions', on_delete=models.PROTECT, verbose_name=_('Mavzu'))
    question = models.TextField(_('Savol'))

    class Meta:
        verbose_name = _('Savol')
        verbose_name_plural = _('Savollar')

    def clean(self):
        if not self.subject.topics.contains(self.topic):
            raise ValidationError({'topic': 'Fanda bunday mavzu mavjud emas.'})

    def __str__(self):
        pass


class Choice(models.Model):
    question = models.ForeignKey('tests.Question', related_name='choices', on_delete=models.CASCADE, verbose_name=_('Savol'))
    letter = models.CharField(_('Variant'), choices=Letters.choices)
    choice = models.CharField(_('Javob'), max_length=128)
    is_correct = models.BooleanField(_('To\'g\'ri javobmi?'), default=False)

    class Meta:
        verbose_name = _('Javob')
        verbose_name_plural = _('Javoblar')
        unique_together = ['question', 'letter']

    def save(self, *args, **kwargs):
        if self.is_correct and self.question.choices.exclude(pk=self.pk).filter(is_correct=True).exists():
            self.question.choices.exclude(pk=self.pk).filter(is_correct=True).update(is_correct=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.question} - {self.letter} - {self.choice}'


__all__ = ['QuestionType', 'Question', 'Choice']

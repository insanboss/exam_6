from django.db import models

# Create your models here.
status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Page(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(max_length=50, null=False,  blank=False, verbose_name='email')
    note_text = models.TextField(null=True, blank=True, verbose_name='Дата')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=50, null=False, blank=False, choices=status_choices, default='active', verbose_name='status')

    def __str__(self):
        return "{}. {}".format(self.pk, self.author)

from django.db import models

# Create your models here.
class Basesettings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    facebook = models.URLField(
        verbose_name='Cыллка на facebook'
    )
    github = models.URLField(
        verbose_name='Cыллка на github'
    )
    twitter = models.URLField(
        verbose_name='Cыллка на twitter'
    )
    google = models.URLField(
        verbose_name='Cыллка на google'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Основная настройка сайта'
        verbose_name_plural = 'Оснавные настройки сайта'
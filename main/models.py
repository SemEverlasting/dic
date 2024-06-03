from django.db import models

class English(models.Model):
    category = models.CharField(max_length=100, verbose_name='категория')
    name = models.CharField(max_length=100, verbose_name='название на английском')
    translate = models.CharField(max_length=100, verbose_name='название на русском')
    translate_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='название на кыргызском')
    image = models.ImageField(upload_to='image', verbose_name='изображения')
    audio = models.FileField(upload_to='audio', blank=True, null=True, verbose_name='аудио')
    video = models.FileField(upload_to='video', blank=True, null=True, verbose_name='видео')
    description = models.TextField(max_length=10000, blank=True, null=True, verbose_name='описание, если потребуется')

    def __str__(self):
        return f' {self.name} - {self.translate}'

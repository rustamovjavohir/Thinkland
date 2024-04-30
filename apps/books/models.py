from django.db import models

from apps.auth_user.models import Authors
from utils.models import SlugModel, BaseModel


class BookManager(models.Manager):

    def book_with_images(self):
        return self.get_queryset().filter(images__isnull=False).distinct()


class BookImages(BaseModel):
    image = models.ImageField(upload_to='books/',
                              verbose_name='Изображение')
    alt = models.CharField(max_length=255,
                           verbose_name='Альтернативный текст')
    title = models.CharField(max_length=255,
                             verbose_name='Заголовок')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.title


class Books(SlugModel):
    images = models.ManyToManyField(BookImages,
                                    related_name='books',
                                    blank=True,
                                    verbose_name='Изображение')
    authors = models.ManyToManyField(Authors,
                                     verbose_name='Авторы')
    published = models.DateField(verbose_name='Дата публикации')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание')

    # Custom manager
    objects = BookManager()

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name

    # first_image property
    @property
    def first_image(self):
        return getattr(getattr(self.images.first(), 'image', None), 'url', None)

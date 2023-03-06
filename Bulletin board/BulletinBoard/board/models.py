from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    Tanks = 'Танки'
    Healers = 'Хилы'
    DD = 'ДД'
    Traders = 'Торговцы'
    GM = 'Гилдмастеры'
    QG = 'Квестгиверы'
    BM = 'Кузнецы'
    LE = 'Кожевники'
    PO = 'Зельевары'
    MS = 'Мастера заклинаний'
    CATEGORY = [
        (Tanks, 'Танки'),
        (Healers, 'Хилы'),
        (Traders, 'Торговцы'),
        (GM, 'Гилдмастеры'),
        (QG, 'Квестгиверы'),
        (BM, 'Кузнецы'),
        (LE, 'Кожевники'),
        (PO, 'Зельевары'),
        (MS, 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=18, choices=CATEGORY, verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, verbose_name='Название')
    text = RichTextField()

    # def __str__(self):
    #     return self.title
    #
    # def get_absolute_url(self):
    #     return reverse('post', args=[str(self.id)])
    #
    # def preview(self):
    #     return '{}...'.format(self.post_text[:124])


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.text

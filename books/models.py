from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Employees(models.Model):


    GENRE = (
        ('action movie', 'action movie'),
        ('romance', 'romance'),
        ('Fantastic', 'Fantastic'),
        ('Mystic', 'Mystic'),
    )
    name = models. CharField(max_length=100, verbose_name="Название книги",null=True)
    email = models.EmailField(default='@gmail.com', verbose_name="Ваша почта",null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите фото', null=True)
    about_emp = models.TextField(verbose_name="о этом книге",null=True)
    programming_status = models.CharField(max_length=100, choices=GENRE,verbose_name="Жанр книги" ,null=True)
    rezume = models.FileField(upload_to='rezume/', verbose_name='Загрузите резюме(необизательно)', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата создание", null=True)
    github = models.URLField(max_length=200, verbose_name="Ссылка на книгу", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата опубликования", null=True)

    def __str__(self):
        return f'{self.name}-{self.programming_status}'


    class Meta:
        verbose_name = 'сотрудника'
        verbose_name_plural = 'сотрудники'
# Create your models here.


class Rewiews(models.Model):
    reviews_book = models.ForeignKey(Employees, on_delete=models.CASCADE,
                                     related_name='reviews_book')
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stars}-{self.reviews_book}'



class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class library(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=100)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
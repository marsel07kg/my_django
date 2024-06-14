from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Employees(models.Model):


    PROGRAMMING_STATUS = (
        ('Full Stack', 'Full Stack'),
        ('Backend Development', 'Backend Development'),
        ('UX-UI Development', 'UX-UI Development'),
        ('Frontend Development', 'Frontend Development'),
    )
    name = models. CharField(max_length=100)
    email = models.EmailField(default='@gmail.com')
    image = models.ImageField(upload_to='images/')
    about_emp = models.TextField()
    programming_status = models.CharField(max_length=100, choices=PROGRAMMING_STATUS, null=True)
    rezume = models.FileField(upload_to='rezume/')
    date_of_birth = models.DateField()
    github = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

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
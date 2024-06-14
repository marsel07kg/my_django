# Generated by Django 5.0.6 on 2024-06-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_employees_programming_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='about_emp',
            field=models.TextField(null=True, verbose_name='о этом книге'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата опубликования'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='Дата создание'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.EmailField(default='@gmail.com', max_length=254, null=True, verbose_name='Ваша почта'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='github',
            field=models.URLField(null=True, verbose_name='Ссылка на книгу'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='programming_status',
            field=models.CharField(choices=[('action movie', 'action movie'), ('romance', 'romance'), ('Fantastic', 'Fantastic'), ('Mystic', 'Mystic')], max_length=100, null=True, verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='rezume',
            field=models.FileField(blank=True, null=True, upload_to='rezume/', verbose_name='Загрузите резюме(необизательно)'),
        ),
    ]
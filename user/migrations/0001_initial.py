# Generated by Django 4.1.3 on 2022-11-29 02:40

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('username',),
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=300, verbose_name='Текст комментария')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.bloguser')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'комментарии',
                'ordering': ('create_at',),
            },
        ),
    ]

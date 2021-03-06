# Generated by Django 3.2.12 on 2022-04-21 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('site_url', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('constricts', models.TextField()),
                ('examples', models.TextField()),
                ('level', models.CharField(max_length=3)),
                ('like_users', models.ManyToManyField(related_name='like_algorithms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solution_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint', models.TextField()),
                ('description', models.TextField()),
                ('solution_code', models.TextField()),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algorithms.algorithm')),
                ('like_users', models.ManyToManyField(related_name='like_solutions', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

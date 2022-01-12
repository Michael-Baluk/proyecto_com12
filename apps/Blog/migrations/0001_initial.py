# Generated by Django 3.2.9 on 2022-01-12 23:30

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'blog_categoria',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('excerpt', models.TextField(max_length=200, null=True)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(max_length=250, unique=True, unique_for_date='publicado')),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='borrador', max_length=10)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Blog.blogcategoria')),
                ('likes', models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'blog_post',
                'ordering': ('-publicado',),
            },
        ),
        migrations.CreateModel(
            name='BlogComentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('contenido', models.TextField(max_length=500)),
                ('publicado', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Blog.blogpost')),
            ],
            options={
                'db_table': 'blog_comentario',
                'ordering': ('-publicado',),
            },
        ),
    ]

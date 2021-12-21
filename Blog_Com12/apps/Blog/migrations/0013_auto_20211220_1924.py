# Generated by Django 3.2.9 on 2021-12-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_alter_blogpost_excerpt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-fecha',)},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='publicado',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='excerpt',
            field=models.TextField(max_length=200, null=True),
        ),
    ]

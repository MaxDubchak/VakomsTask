# Generated by Django 2.1.7 on 2019-03-15 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_name',
            new_name='name',
        ),
    ]

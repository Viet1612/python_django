# Generated by Django 3.2 on 2021-05-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_django', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
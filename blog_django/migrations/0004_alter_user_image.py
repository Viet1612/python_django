# Generated by Django 3.2 on 2021-05-25 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_django', '0003_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/%Y/%m/%d/'),
        ),
    ]

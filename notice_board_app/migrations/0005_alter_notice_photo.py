# Generated by Django 4.2.6 on 2023-10-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOTICEBOARD', '0004_alter_notice_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='photo',
            field=models.ImageField(null=True, upload_to='Photos/'),
        ),
    ]

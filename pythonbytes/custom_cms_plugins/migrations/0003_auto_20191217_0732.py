# Generated by Django 2.2.8 on 2019-12-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_cms_plugins', '0002_cardplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardplugin',
            name='title_tag',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='cardplugin',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 2.2.8 on 2019-12-25 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20191221_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='unsubscribe_key',
            field=models.CharField(default='ooDGV1WZeSJ6stmojNDAVOKFzVQ', editable=False, max_length=50),
        ),
    ]
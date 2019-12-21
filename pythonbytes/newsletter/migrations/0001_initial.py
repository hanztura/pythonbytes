# Generated by Django 2.2.8 on 2019-12-17 08:35

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import djangocms_text_ckeditor.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=50)),
                ('body', djangocms_text_ckeditor.fields.HTMLField()),
                ('is_delivered', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email_address', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_success', models.BooleanField(blank=True, default=False)),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscribers', to='newsletter.Newsletter')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='newsletters', to='newsletter.Subscriber')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

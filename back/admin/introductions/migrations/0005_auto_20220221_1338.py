# Generated by Django 3.2.12 on 2022-02-21 13:38

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('introductions', '0004_remove_introduction_polymorphic_ctype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduction',
            name='intro_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Person to introduce'),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='name',
            field=models.CharField(max_length=240, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10200), blank=True, size=None, verbose_name='Tags'),
        ),
    ]

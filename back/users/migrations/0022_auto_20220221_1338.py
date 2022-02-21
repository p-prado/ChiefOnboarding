# Generated by Django 3.2.12 on 2022-02-21 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0004_auto_20210511_1242'),
        ('users', '0021_alter_preboardinguser_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='buddy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='new_hire_buddy', to=settings.AUTH_USER_MODEL, verbose_name='Buddy'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('nl', 'Dutch'), ('fr', 'French'), ('de', 'German'), ('tr', 'Turkish'), ('pt', 'Portuguese'), ('es', 'Spanish')], default='en', max_length=5, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='linkedin',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='new_hire_manager', to=settings.AUTH_USER_MODEL, verbose_name='Manager'),
        ),
        migrations.AlterField(
            model_name='user',
            name='message',
            field=models.TextField(blank=True, default='', verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='misc.file', verbose_name='Profile image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'New Hire'), (1, 'Administrator'), (2, 'Manager'), (3, 'Other')], default=3, help_text='An administrator has access to everything. A manager has only access to their new hires and their tasks.', verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='start_day',
            field=models.DateField(blank=True, help_text='First working day', null=True, verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='timezone',
            field=models.CharField(default='', max_length=1000, verbose_name='Timezone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Twitter'),
        ),
    ]

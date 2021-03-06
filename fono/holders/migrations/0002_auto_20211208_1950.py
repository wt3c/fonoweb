# Generated by Django 3.2.9 on 2021-12-08 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='holder',
            options={'verbose_name': 'titular', 'verbose_name_plural': 'titulares'},
        ),
        migrations.AddField(
            model_name='holder',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='holder',
            name='cod_ecad',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cód.ECAD'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-10 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('holders', '0006_auto_20211210_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holder',
            name='pseudonyms',
        ),
        migrations.RemoveField(
            model_name='pseudonym',
            name='owner',
        ),
        migrations.AddField(
            model_name='pseudonym',
            name='holder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='holders.holder', verbose_name='Titular'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-13 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_correspondencia_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='correspondencia',
            name='mensaje',
            field=models.CharField(default='Ingresar mensaje...', max_length=600),
        ),
    ]

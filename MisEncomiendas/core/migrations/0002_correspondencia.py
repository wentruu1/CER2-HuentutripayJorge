# Generated by Django 4.1.3 on 2022-11-13 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correspondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.residencia')),
            ],
        ),
    ]

# Generated by Django 2.0.6 on 2018-08-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cisternas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cisterna',
            name='litros',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cisterna',
            name='ultima_medicao',
            field=models.DateTimeField(null=True, verbose_name='ultima medicao'),
        ),
    ]

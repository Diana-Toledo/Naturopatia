# Generated by Django 2.2.10 on 2020-05-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200513_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradablog',
            name='descripcion_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='entradablog',
            name='descripcion_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='entradablog',
            name='titulo_en',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='entradablog',
            name='titulo_es',
            field=models.CharField(max_length=70, null=True),
        ),
    ]

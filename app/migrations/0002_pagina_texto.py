# Generated by Django 2.2.10 on 2020-03-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagina',
            name='texto',
            field=models.TextField(null=True),
        ),
    ]
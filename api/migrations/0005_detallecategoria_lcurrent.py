# Generated by Django 5.1.4 on 2024-12-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_imagen_curl'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecategoria',
            name='lCurrent',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

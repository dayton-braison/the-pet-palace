# Generated by Django 4.2.2 on 2023-08-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='breed',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]

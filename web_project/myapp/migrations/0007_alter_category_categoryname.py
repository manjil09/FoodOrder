# Generated by Django 4.2.7 on 2024-01-12 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_food_varietyoptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CategoryName',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_category_food_order_customuser_registerdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='VarietyOptions',
            field=models.JSONField(default=list),
        ),
    ]

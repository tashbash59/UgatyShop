# Generated by Django 3.1.6 on 2022-04-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_card_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
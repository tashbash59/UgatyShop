# Generated by Django 3.1.6 on 2022-04-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220402_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, max_digits=2)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('футболки', 'футболки'), ('кофты', 'кофты'), ('другое', 'другое')], default='другое', max_length=9),
        ),
    ]

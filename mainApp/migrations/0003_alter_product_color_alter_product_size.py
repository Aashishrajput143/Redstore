# Generated by Django 4.0.4 on 2022-05-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_buyer_pic_alter_product_pic1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=150),
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-11 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('shipping', models.IntegerField()),
                ('final', models.IntegerField()),
                ('mode', models.CharField(max_length=20)),
                ('orderstatus', models.IntegerField(choices=[(0, 'Cancel'), (1, 'Not Packed'), (2, 'Packed'), (3, 'Out for Delivery'), (4, 'Delivered')], default=1)),
                ('paymentstatus', models.IntegerField(choices=[(1, 'Pending'), (2, 'Done')], default=1)),
                ('rppid', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('rpoid', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('rpsid', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='CheckoutProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total', models.IntegerField()),
                ('pic', models.FileField(blank=True, default='noimage.jpg', null=True, upload_to='images')),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.checkout')),
            ],
        ),
    ]

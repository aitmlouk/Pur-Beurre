# Generated by Django 2.2.4 on 2019-11-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ean', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(default='products_default.jpg', upload_to='products_pics')),
                ('nutriscore', models.CharField(max_length=100)),
            ],
        ),
    ]
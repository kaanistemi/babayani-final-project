# Generated by Django 3.0.8 on 2020-09-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(blank=True, choices=[('All Prducts', 'All Products'), ('Homeware', 'Homeware'), ('Accessories and Gifts', 'Accessories and Gifts'), ('Special Offers', 'Special Offers')], max_length=100)),
                ('page_text', models.TextField(blank=True)),
            ],
        ),
    ]

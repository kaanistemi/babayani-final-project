# Generated by Django 3.0.8 on 2020-09-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_pagetext_heading'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagetext',
            old_name='heading',
            new_name='heading1',
        ),
        migrations.AddField(
            model_name='pagetext',
            name='heading2',
            field=models.TextField(blank=True),
        ),
    ]

    

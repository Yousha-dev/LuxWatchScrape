# Generated by Django 4.2.9 on 2024-01-29 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_ref_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]

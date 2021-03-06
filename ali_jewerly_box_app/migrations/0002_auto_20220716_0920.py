# Generated by Django 3.2.9 on 2022-07-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ali_jewerly_box_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ICED WATCH', 'ICED WATCH'), ('LEATHER WATCH', 'LEATHER WATCH'), ('NECKLACE', 'NECKLACE'), ('RINGs', 'RING'), ('GRILL', 'GRILL')], default='ICED WATCH', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]

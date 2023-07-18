# Generated by Django 3.1.5 on 2023-01-09 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_auto_20230106_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='is_best',
            field=models.BooleanField(blank=True, default=False, help_text='매장의 대표메뉴 인지', null=True, verbose_name='대표 메뉴 여부'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='is_popular',
            field=models.BooleanField(blank=True, default=False, help_text='매장의 인기 메뉴인지', null=True, verbose_name='인기 메뉴 여부'),
        ),
    ]

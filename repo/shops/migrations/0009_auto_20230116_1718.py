# Generated by Django 3.1.5 on 2023-01-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0008_auto_20230116_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopscore',
            name='enfa_score',
            field=models.SmallIntegerField(default=50, verbose_name='ENFA 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='enfc_score',
            field=models.SmallIntegerField(default=50, verbose_name='ENFC 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='enta_score',
            field=models.SmallIntegerField(default=50, verbose_name='ENTA 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='entc_score',
            field=models.SmallIntegerField(default=50, verbose_name='ENTC 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='esfa_score',
            field=models.SmallIntegerField(default=50, verbose_name='ESFA 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='esfc_score',
            field=models.SmallIntegerField(default=50, verbose_name='ESFC 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='esta_score',
            field=models.SmallIntegerField(default=50, verbose_name='ESTA 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='estc_score',
            field=models.SmallIntegerField(default=50, verbose_name='ESTC 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='infa_score',
            field=models.SmallIntegerField(default=50, verbose_name='INFA 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='infc_score',
            field=models.SmallIntegerField(default=50, verbose_name='INFC 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='inta_score',
            field=models.SmallIntegerField(default=50, verbose_name='INTA 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='intc_score',
            field=models.SmallIntegerField(default=50, verbose_name='INTC 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='isfa_score',
            field=models.SmallIntegerField(default=50, verbose_name='ISFA 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='isfc_score',
            field=models.SmallIntegerField(default=50, verbose_name='ISFC 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='ista_score',
            field=models.SmallIntegerField(default=50, verbose_name='ISTA 점수'),
        ),
        migrations.AlterField(
            model_name='shopscore',
            name='istc_score',
            field=models.SmallIntegerField(default=50, verbose_name='ISTC 점수'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avcadastro', '0006_auto_20201109_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalheindicador',
            name='modoindicador',
            field=models.CharField(choices=[('CSM', 'CALCULO SOMA'), ('CSB', 'CALCULO SUBTRAI'), ('CMU', 'CALCULO MULTIPLICA'), ('CDI', 'CALCULO DIVIDE'), ('UNI', 'UNITARIO'), ('CON', 'CONTAR'), ('NDA', 'NAO FAZ PARTE')], max_length=3),
        ),
    ]

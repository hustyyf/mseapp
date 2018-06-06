# Generated by Django 2.0.2 on 2018-03-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(choices=[('129', '14栋129'), ('136', '14栋136'), ('138', '14栋136'), ('345', '14栋345')], default='136', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('y', 'usable'), ('n', 'unusable')], default='y', max_length=2),
            preserve_default=False,
        ),
    ]

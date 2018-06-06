# Generated by Django 2.0.2 on 2018-03-06 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.CharField(max_length=10)),
                ('apply_date', models.DateTimeField(auto_now_add=True)),
                ('aim_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('stop_time', models.TimeField()),
                ('phone_num', models.CharField(max_length=11)),
                ('apply_reason', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='rent',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicroom.Room'),
        ),
    ]
# Generated by Django 2.0.4 on 2018-05-11 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fasongzhe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('fnumber', models.IntegerField()),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='jieshouzhe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jname', models.CharField(max_length=20)),
                ('jnumber', models.IntegerField()),
                ('jfasongzhe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fasongzhe')),
            ],
        ),
    ]

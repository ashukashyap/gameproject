# Generated by Django 3.0.4 on 2020-09-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200910_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('deshwer', models.CharField(max_length=100)),
                ('fridabad', models.CharField(max_length=200)),
                ('gaziybad', models.CharField(max_length=100)),
                ('gali', models.CharField(max_length=200)),
                ('shrignash', models.CharField(max_length=100)),
                ('delhibazzer', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.2.18 on 2022-04-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailId', models.EmailField(max_length=254)),
                ('ssc_p', models.CharField(max_length=30)),
                ('ssc_b', models.CharField(max_length=30)),
                ('hsc_p', models.CharField(max_length=30)),
                ('hsc_b', models.CharField(max_length=30)),
                ('hsc_s', models.CharField(max_length=30)),
                ('degree_p', models.CharField(max_length=30)),
                ('degree_t', models.CharField(max_length=30)),
                ('workex', models.CharField(max_length=30)),
            ],
        ),
    ]

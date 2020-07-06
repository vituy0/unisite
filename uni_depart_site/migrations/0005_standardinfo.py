# Generated by Django 2.2.6 on 2020-05-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_depart_site', '0004_uniinfo_uni_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_max_field', models.CharField(max_length=20, null=True, verbose_name='max_field')),
                ('standard_mid_field', models.CharField(max_length=20, null=True, verbose_name='mid_field')),
                ('standard_min_field', models.CharField(max_length=20, null=True, verbose_name='min_field')),
            ],
        ),
    ]
# Generated by Django 3.1 on 2020-09-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampusImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtype', models.CharField(max_length=100)),
                ('imgurl', models.CharField(max_length=999)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False, verbose_name='身份证')),
                ('sname', models.CharField(db_index=True, max_length=100, verbose_name='姓名')),
                ('scard', models.CharField(max_length=100, verbose_name='学号')),
                ('shouse', models.CharField(blank=True, default=None, max_length=100)),
                ('sroom', models.CharField(max_length=100)),
                ('smajor', models.CharField(blank=True, default=None, max_length=100)),
                ('sclass', models.CharField(blank=True, default=None, max_length=100)),
                ('sbed', models.CharField(blank=True, default=None, max_length=100)),
            ],
        ),
    ]

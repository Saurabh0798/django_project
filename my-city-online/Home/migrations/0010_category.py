# Generated by Django 3.2.3 on 2021-06-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_alter_contactus_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=20)),
                ('Curl', models.CharField(max_length=20)),
                ('Cimage', models.ImageField(upload_to='cimage')),
            ],
        ),
    ]
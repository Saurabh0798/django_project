# Generated by Django 3.2.3 on 2021-06-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_advocates_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Mobile', models.IntegerField(max_length=11)),
                ('City', models.CharField(max_length=20)),
            ],
        ),
    ]

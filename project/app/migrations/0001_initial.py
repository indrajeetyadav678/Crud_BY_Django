# Generated by Django 5.0.6 on 2024-05-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmplayeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Number', models.CharField(max_length=8)),
                ('Position', models.CharField(max_length=30)),
                ('Sallary', models.IntegerField()),
            ],
        ),
    ]
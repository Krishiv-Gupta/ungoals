# Generated by Django 4.1.3 on 2024-04-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cheatcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('W', models.CharField(max_length=500)),
            ],
        ),
    ]
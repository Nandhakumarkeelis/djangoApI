# Generated by Django 5.0.7 on 2024-07-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=100)),
            ],
        ),
    ]
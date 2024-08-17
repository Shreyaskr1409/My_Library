# Generated by Django 5.0.6 on 2024-06-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('heading', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('publisher', models.CharField(max_length=100)),
                ('date_published', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-10 07:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_readlatercart_delete_userselection"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="book_id",
        ),
        migrations.AddField(
            model_name="book",
            name="id",
            field=models.CharField(
                default="0000000000000",
                max_length=13,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(default="", unique=True),
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "books",
                    models.ManyToManyField(related_name="in_carts", to="base.book"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ReadLaterCart",
        ),
    ]
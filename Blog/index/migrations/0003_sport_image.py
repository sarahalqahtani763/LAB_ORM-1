# Generated by Django 4.2.7 on 2023-11-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0002_alter_sport_published_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="sport",
            name="image",
            field=models.ImageField(default="images/default.jpg", upload_to="images/"),
        ),
    ]

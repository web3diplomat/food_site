# Generated by Django 4.1.7 on 2023-02-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8GV0f6prb-DPesR3lFwG2UsJh94yNz7ijRQ&usqp=CAU",
                max_length=500,
            ),
        ),
    ]
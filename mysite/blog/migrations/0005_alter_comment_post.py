# Generated by Django 5.1.7 on 2025-03-28 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_comment_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="blog.post"
            ),
        ),
    ]

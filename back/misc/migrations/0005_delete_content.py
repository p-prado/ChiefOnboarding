# Generated by Django 3.2.12 on 2022-02-24 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("misc", "0004_auto_20210511_1242"),
        ("to_do", "0004_todo_content_json"),
        ("preboarding", "0008_auto_20220209_0048"),
        ("badges", "0004_badge_content_json"),
        ("resources", "0007_auto_20220210_2223"),
        ("sequences", "0020_rename_content_json2_externalmessage_content_json"),
        ("sequences", "0020_rename_content_json2_externalmessage_content_json"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Content",
        ),
    ]

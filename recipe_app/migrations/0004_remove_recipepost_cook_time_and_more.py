# Generated by Django 4.1.5 on 2023-02-08 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0003_alter_recipecomments_comment_img_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipepost',
            name='cook_time',
        ),
        migrations.RemoveField(
            model_name='recipepost',
            name='prep_time',
        ),
        migrations.AddField(
            model_name='recipepost',
            name='cook_time_minute',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipepost',
            name='prep_time_minute',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipepost',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
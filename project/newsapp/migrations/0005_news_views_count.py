# Generated by Django 4.0.3 on 2022-07-05 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_alter_news_category_alter_news_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
    ]

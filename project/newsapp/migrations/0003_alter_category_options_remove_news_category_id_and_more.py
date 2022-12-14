# Generated by Django 4.0.3 on 2022-06-17 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_alter_news_category_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='category_id',
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, db_column='category_id', null=True, on_delete=django.db.models.deletion.PROTECT, to='newsapp.category'),
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

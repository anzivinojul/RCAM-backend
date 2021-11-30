# Generated by Django 3.2.9 on 2021-11-16 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('recette', '0002_alter_recette_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='recette',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.categorierecette'),
        ),
        migrations.AddField(
            model_name='recette',
            name='img',
            field=models.ImageField(null=True, upload_to='recette_img'),
        ),
    ]
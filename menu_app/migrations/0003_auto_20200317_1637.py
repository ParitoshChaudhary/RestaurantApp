# Generated by Django 2.2.10 on 2020-03-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_auto_20200302_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete='models.CASCADE', to='menu_app.Category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cuisine',
            field=models.ForeignKey(on_delete='models.CASCADE', to='menu_app.Cuisine'),
        ),
    ]
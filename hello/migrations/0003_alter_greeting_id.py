# Generated by Django 3.2 on 2021-04-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_alter_greeting_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greeting',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 5.0.7 on 2024-08-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommersapp', '0005_alter_useraccount_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommersapp', '0003_alter_useraccount_email_alter_useraccount_mobileno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.BinaryField(),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0005_alter_party_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='Mobile_no',
            field=models.IntegerField(default=True, max_length=10),
        ),
    ]
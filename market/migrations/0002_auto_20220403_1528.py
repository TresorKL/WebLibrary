# Generated by Django 3.1.7 on 2022-04-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.IntegerField(),
        ),
    ]

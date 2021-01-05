# Generated by Django 3.0.8 on 2020-10-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_remove_profile_describeyourself'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]
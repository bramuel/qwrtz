# Generated by Django 2.2 on 2021-06-28 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepapp', '0006_productsearch_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userInfo', models.CharField(max_length=255)),
                ('ids', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-14 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_skills_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_no', models.TextField(blank=True)),
                ('village_name', models.TextField(blank=True)),
            ],
        ),
    ]

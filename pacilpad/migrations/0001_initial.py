# Generated by Django 4.1.3 on 2022-11-27 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.IntegerField()),
                ('synopsis', models.TextField()),
                ('page', models.IntegerField()),
                ('cover', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacilpad.publisher')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacilpad.writer')),
            ],
        ),
    ]

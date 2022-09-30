# Generated by Django 4.1 on 2022-09-30 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsSalta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=40)),
                ('cuerpo', models.CharField(max_length=300)),
                ('autor', models.CharField(max_length=40)),
                ('fecha', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogsalta')),
            ],
        ),
    ]

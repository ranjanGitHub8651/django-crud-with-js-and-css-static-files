# Generated by Django 3.2.12 on 2023-03-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=200)),
                ('designation', models.CharField(choices=[('WEB DEVELOPER', 'WEB DEVELOPER'), ('PYTHON DEVELOPER', 'PYTHON DEVELOPER'), ('DJANGO DEVELOPER', 'DJANGO DEVELOPER'), ('PYTHON & DJANGO DEVELOPER', 'PYTHON & DJANGO DEVELOPER'), ('FULLSTACK DEVELOPER', 'FULLSTACK DEVELOPER'), ('JAVA DEVELOPER', 'JAVA DEVELOPER'), ('FRONTEND DEVELOPER', 'FRONTEND DEVELOPER'), ('OTHER DEVELOPER', 'OTHER DEVELOPER')], default='PYTHON DEVELOPER', max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-04-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(help_text='Enter user_name', max_length=20)),
                ('emailField', models.CharField(help_text='Enter emailField', max_length=20)),
                ('password', models.CharField(help_text='Enter password', max_length=20)),
            ],
            options={
                'verbose_name': 'user_auth',
                'verbose_name_plural': 'user_auths',
            },
        ),
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(help_text='Enter user_name', max_length=20)),
                ('first_name', models.CharField(help_text='Enter first_name', max_length=20)),
                ('last_name', models.CharField(help_text='Enter last_name', max_length=20)),
                ('number', models.CharField(help_text='Enter number', max_length=20)),
                ('email', models.EmailField(help_text='Enter email', max_length=25)),
                ('designation', models.CharField(help_text='Enter designation', max_length=20)),
                ('department', models.CharField(help_text='Enter department', max_length=20)),
            ],
        ),
    ]

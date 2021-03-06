# Generated by Django 3.0.8 on 2020-09-16 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesCompleted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Service Date')),
                ('service', models.CharField(choices=[('O', 'Oil Service'), ('T', 'Tire Service'), ('X', 'Other Service')], default='X', max_length=1)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Car')),
            ],
        ),
    ]

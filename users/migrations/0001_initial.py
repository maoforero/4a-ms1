# Generated by Django 3.2.7 on 2021-11-16 21:16

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Admin', 'Administrador'), ('User', 'Usuario'), ('Inv', 'Invitado')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('typeid', models.CharField(choices=[('CC', 'Cédula de ciudadania'), ('CE', 'Cédula de extranjería')], max_length=10)),
                ('numberid', models.CharField(blank=True, max_length=12)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('birth', models.DateField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=12)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
            ],
        ),
    ]
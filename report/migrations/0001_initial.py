# Generated by Django 2.2.1 on 2019-06-24 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Disabled'), ('R', 'Retired'), ('U', 'Unresponsive'), ('X', 'Unused')], max_length=3)),
                ('desired_accuracy', models.DecimalField(decimal_places=1, max_digits=5)),
                ('location_method', models.CharField(choices=[('G', 'GPS'), ('L', 'LTE'), ('B', 'GPS+LTE')], default=('B', 'GPS+LTE'), max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='date time recorded')),
                ('geo_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('geo_long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('geo_accuracy', models.DecimalField(decimal_places=1, max_digits=5)),
                ('tracker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Tracker')),
            ],
        ),
    ]

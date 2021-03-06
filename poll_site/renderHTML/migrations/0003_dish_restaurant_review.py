# Generated by Django 2.1.3 on 2018-12-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renderHTML', '0002_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Euro amount')),
                ('image', models.ImageField(upload_to='myrestaurants')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('street', models.TextField()),
                ('number', models.IntegerField()),
                ('city', models.TextField(default='')),
                ('zipcode', models.IntegerField()),
                ('stateorProvince', models.TextField()),
                ('country', models.TextField()),
                ('telephone', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], verbose_name='Rating (stars)')),
                ('comment', models.TextField()),
            ],
        ),
    ]

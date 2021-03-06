# Generated by Django 2.1.4 on 2018-12-07 05:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('renderHTML', '0003_dish_restaurant_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='dish',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='renderHTML.Restaurant'),
        ),
        migrations.AddField(
            model_name='dish',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

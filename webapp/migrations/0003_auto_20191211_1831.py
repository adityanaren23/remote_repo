# Generated by Django 3.0 on 2019-12-12 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_feedbackdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdata',
            name='date',
            field=models.DateTimeField(auto_now_add=True, max_length=50),
        ),
    ]

# Generated by Django 3.0 on 2019-12-12 12:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_contactdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='branches',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Hyd', 'HYDERABAD'), ('Pune', 'PUNE'), ('Bang', 'BANGALORE')], max_length=300),
        ),
    ]

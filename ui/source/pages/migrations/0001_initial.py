# Generated by Django 3.1.1 on 2020-10-15 04:20

from django.db import migrations, models
import encrypted_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputs', encrypted_fields.fields.EncryptedTextField()),
                ('script', models.TextField()),
            ],
        ),
    ]

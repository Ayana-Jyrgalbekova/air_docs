# Generated by Django 4.0.1 on 2022-01-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_client_documents_fio'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.TextField()),
                ('when', models.CharField(max_length=255)),
            ],
        ),
    ]
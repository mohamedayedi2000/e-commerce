# Generated by Django 4.1.7 on 2023-05-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0015_alter_project_date_fin'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_debut',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='date_fin',
            field=models.TextField(),
        ),
    ]
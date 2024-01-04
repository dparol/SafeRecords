# Generated by Django 5.0.1 on 2024-01-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_businessmanager_businessemployee_qrcoedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcoedata',
            name='com_note',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='qrcoedata',
            name='quality',
            field=models.CharField(choices=[('good', 'GOOD'), ('damaged', 'Damaged')], max_length=100),
        ),
    ]
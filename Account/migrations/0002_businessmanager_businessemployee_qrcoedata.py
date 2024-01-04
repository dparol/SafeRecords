# Generated by Django 5.0.1 on 2024-01-03 12:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('managerId', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=50)),
                ('emp_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('emp_IdCard', models.ImageField(upload_to=None)),
                ('managerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.businessmanager')),
            ],
        ),
        migrations.CreateModel(
            name='QrCoeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=50)),
                ('item_id', models.CharField(max_length=50)),
                ('quality', models.CharField(max_length=100)),
                ('com_note', models.TextField(choices=[('good', 'GOOD'), ('damaged', 'Damaged')], max_length=100)),
                ('item_status', models.CharField(choices=[('checked', 'CHECKED'), ('unchecked', 'UNCHECKED')], default='unckecked', max_length=50)),
                ('empId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.businessemployee')),
            ],
        ),
    ]
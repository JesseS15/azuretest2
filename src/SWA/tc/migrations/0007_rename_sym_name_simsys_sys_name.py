# Generated by Django 4.1.2 on 2022-12-02 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tc', '0006_simsys_sim_sim_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simsys',
            old_name='sym_name',
            new_name='sys_name',
        ),
    ]

# Generated by Django 4.1.2 on 2022-12-02 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tc', '0007_rename_sym_name_simsys_sys_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sim',
            old_name='sim_list',
            new_name='sys_list',
        ),
    ]

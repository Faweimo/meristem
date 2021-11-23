# Generated by Django 3.2.9 on 2021-11-23 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_alter_clientdetail_bank_name_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetail',
            name='account_number_3bank_name_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='bank_name_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Bank3', to='client.bankname'),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='branch_3bank_name_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
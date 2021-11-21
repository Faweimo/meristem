# Generated by Django 3.2.9 on 2021-11-20 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_auto_20211120_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdetail',
            name='bankdetail',
        ),
        migrations.RemoveField(
            model_name='clientdetail',
            name='beneficiary_details',
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='account_number_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='address_beneficiary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='address_beneficiary_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='bank_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.bankname'),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='bank_name_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='bank_name_beneficiary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='bank_name_beneficiary_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='branch_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='full_name_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='phone_number_beneficiary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientdetail',
            name='phone_number_beneficiary_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='BankDetail',
        ),
        migrations.DeleteModel(
            name='BeneficiaryDetail',
        ),
    ]

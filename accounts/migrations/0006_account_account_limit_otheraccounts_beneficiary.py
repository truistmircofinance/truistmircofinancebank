# Generated by Django 4.1.5 on 2024-04-29 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_creditcard_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_limit',
            field=models.IntegerField(blank=True, null=True, verbose_name='Account Limit'),
        ),
        migrations.CreateModel(
            name='OtherAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_number', models.CharField(max_length=10, unique=True, verbose_name='Account Number')),
                ('balance', models.DecimalField(decimal_places=2, default=0, help_text='Client Cleared Account Balance', max_digits=12, verbose_name='Available Balance')),
                ('ledger_balance', models.DecimalField(decimal_places=2, default=0, help_text='Client Uncleared Account Balance', max_digits=12, verbose_name='Ledger Balance')),
                ('last_received', models.DecimalField(decimal_places=2, default=0, help_text='Client wallet Balance', max_digits=12, verbose_name='Wallet Balance')),
                ('currency', models.CharField(blank=True, choices=[('Dollar', 'Dollar'), ('Pounds', 'Pounds')], max_length=15, null=True)),
                ('allow_transfer', models.BooleanField(default=False, help_text='Enable or Disable Transfer  (If Disabled, user account will freeze.)')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_name', models.CharField(blank=True, max_length=50, null=True)),
                ('bank', models.CharField(blank=True, max_length=50, null=True)),
                ('acc_number', models.CharField(max_length=20, unique=True, verbose_name='Account Number')),
                ('rout_number', models.CharField(blank=True, max_length=9, null=True, verbose_name='Routing Number')),
                ('swift_code', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(blank=True, choices=[('Dollar', 'Dollar'), ('Pounds', 'Pounds')], default='Dollar', max_length=15, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Beneficiary',
                'verbose_name_plural': 'Beneficiaries',
            },
        ),
    ]

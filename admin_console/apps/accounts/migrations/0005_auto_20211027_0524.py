# Generated by Django 2.2.6 on 2021-10-27 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211027_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
                ('zip_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ZipCode')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.ManyToManyField(through='accounts.Status', to='accounts.ZipCode'),
        ),
    ]
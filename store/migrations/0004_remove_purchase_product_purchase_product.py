# Generated by Django 4.0.2 on 2022-02-28 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_purchase_product_purchase_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.AddField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='store.product'),
        ),
    ]
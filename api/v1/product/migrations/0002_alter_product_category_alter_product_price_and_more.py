# Generated by Django 4.2.2 on 2023-06-18 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcategory', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Precio del producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(verbose_name='Stock'),
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
        migrations.AlterModelTable(
            name='productcategory',
            table='product_category',
        ),
    ]
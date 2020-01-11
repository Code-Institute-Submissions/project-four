# Generated by Django 2.2.8 on 2020-01-11 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Graphite', 'Graphite'), ('Modern', 'Modern'), ('Metal', 'Metal'), ('Oversize', 'Oversize'), ('Modern', 'Modern')], default='Graphite', max_length=100)),
                ('slug', models.SlugField(null=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Category'),
        ),
    ]
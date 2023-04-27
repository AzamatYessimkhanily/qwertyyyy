# Generated by Django 4.1.7 on 2023-04-26 22:00

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2550)),
                ('image', models.ImageField(upload_to='test1/clothing')),
                ('size', multiselectfield.db.fields.MultiSelectField(choices=[('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('нет в наличий', 'нет в наличий')], max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=150)),
            ],
        ),
    ]
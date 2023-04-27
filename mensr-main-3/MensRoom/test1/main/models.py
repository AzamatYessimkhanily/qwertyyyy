from django.db import models
from multiselectfield import MultiSelectField
from multiselectfield.validators import MaxValueMultiFieldValidator


class Clothing(models.Model):
    name = models.CharField(max_length=2550)
    image = models.ImageField(upload_to='test1/clothing')
    size = MultiSelectField(choices=(('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('нет в наличий', 'нет в наличий')), max_length=200)
    price = models.DecimalField(max_digits=150, decimal_places=2)

    def __str__(self):
        return self.name


Clothing._meta.get_field('size').validators.append(MaxValueMultiFieldValidator(100))

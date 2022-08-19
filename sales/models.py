from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import date
from sales.products import products

class Products(models.Model):
    product_name = models.CharField(max_length=30, choices=products)
    quantity = models.IntegerField()
    expiry_date = models.DateField(default=date.today)
    slug = models.SlugField(null=False, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('products-detail', kwargs={'slug': self.slug})
        #return '/%s/' % self.quantity

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
            return super(Products, self).save(*args, **kwargs)


class Sold(models.Model):
    product = models.OneToOneField(Products, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    product_name = models.CharField(max_length=30, choices=products)
    quantity_sold = models.IntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    note = models.TextField(null=True, blank=True)


    # Display on the admin page as Sold instead of Solds
    class Meta:
        verbose_name_plural = 'Sold'

    def get_absolute_url(self):
        return reverse('sold-date-detail', kwargs={'pk':self.pk})

    def totalAmountOfProduct(self):
        return self.unit_price * self.quantity_sold


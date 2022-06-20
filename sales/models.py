from django.db import models
from django.urls import reverse

pl = open('sales/product_list.txt', 'r')

class Sold(models.Model):
    date = models.DateField()
    product_name = models.CharField(max_length=30, choices = pl)
    quantity_sold = models.IntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    note = models.TextField(null=True, blank=True)


    # Display on the admin page as Sold instead of Solds
    class Meta:
        verbose_name_plural = 'Sold'

    # Customize what is displayed
    #def __str__(self):
        #return f'{self.s_n},{self.date}, {self.product_name},\
                #{self.quantity_sold}, {self.unit_price}, {self.total},\
                #{self.note}'

    def get_absolute_url(self):
        return reverse('sold-date-detail', kwargs={'pk':self.pk})

    def totalAmountOfProduct(self):
        return self.unit_price * self.quantity_sold

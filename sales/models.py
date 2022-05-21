from django.db import models

class Sold(models.Model):
    date = models.DateField()
    product_name = models.CharField(max_length=30)
    quantity_sold = models.IntegerField()
    unit_price = models.IntegerField()
    total = models.IntegerField()
    note = models.TextField(null=True, blank=True)


    # Display on the admin page as Sold instead of Solds
    class Meta:
        verbose_name_plural = 'Sold'

    
    # Customize what is displayed
    def __str__(self):
        return f'{self.date}, {self.product_name}, {self.quantity_sold},\
        {self.unit_price}, {self.total}, {self.note}'

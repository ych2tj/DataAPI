from django.db import models

# finance table
class shareprice(models.Model):
    date = models.DateField()
    open = models.DecimalField(max_digits=6, decimal_places=2)
    high = models.DecimalField(max_digits=6, decimal_places=2)
    low = models.DecimalField(max_digits=6, decimal_places=2)
    close = models.DecimalField(max_digits=6, decimal_places=2)
    volumn = models.PositiveBigIntegerField()
    change = models.DecimalField(max_digits=4, decimal_places=3)
    changePercent = models.DecimalField(max_digits=6, decimal_places=5)
    symbol = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} id:{self.id}"

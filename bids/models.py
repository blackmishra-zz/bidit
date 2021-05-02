from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    price = models.TextField(default='1')
    category = models.TextField(default='Electronics')
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    bids_total = models.IntegerField(default=1)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def decent_date(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    class Meta:
        ordering = ['-pub_date']

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
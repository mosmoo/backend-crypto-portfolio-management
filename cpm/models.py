from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)  # Adjust max_length as needed
    current_price = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return self.name

    # Other fields as needed

class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.portfolio_name
    # Add more fields as needed

class PortfolioToken(models.Model):
    id = models.AutoField(primary_key=True)  # Add this line to explicitly define 'id' as the primary key
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=10)

    # Add more fields as needed

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
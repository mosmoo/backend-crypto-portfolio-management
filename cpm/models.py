from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    token_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)
    current_price = models.DecimalField(max_digits=20, decimal_places=10)
    # Add more fields as needed

class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.portfolio_name
    # Add more fields as needed

class PortfolioToken(models.Model):
    portfolio_token_id = models.AutoField(primary_key=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

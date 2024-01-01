from django.contrib import admin
from .models import UserProfile, Token, PortfolioToken, Portfolio

admin.site.register(UserProfile)
admin.site.register(Token)
admin.site.register(PortfolioToken)
admin.site.register(Portfolio)

# Register your models here.
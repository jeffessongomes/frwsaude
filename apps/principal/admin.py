from django.contrib import admin
from .models import Product, Ingredients, Contact, Initial, How_Use, Video_Description, How_Use_Text, TecDashImages, ProductsPrize

admin.site.register(Product)
admin.site.register(Ingredients)
admin.site.register(Contact)
admin.site.register(Initial)
admin.site.register(How_Use)
admin.site.register(How_Use_Text)
admin.site.register(Video_Description)
admin.site.register(TecDashImages)
admin.site.register(ProductsPrize)
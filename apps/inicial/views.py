from django.shortcuts import render
from .models import Doubt, Client, PhotoProdutoAfterBefore
from apps.principal.models import Product, Ingredients, Contact, Initial
from apps.principal.models import How_Use, Video_Description, How_Use_Text, ProductsPrize

def index(request):
	doubts = Doubt.objects.all()
	clients = Client.objects.all()
	Photo_Product = PhotoProdutoAfterBefore.objects.all()
	products = Product.objects.all()
	initial = Initial.objects.get(pk=1)
	video = Video_Description.objects.get(pk=1)
	hows = How_Use.objects.all()
	how_text = How_Use_Text.objects.get(pk=1)
	ingredients = Ingredients.objects.all()
	product_prizes = ProductsPrize.objects.all()	

	data = {'doubts': doubts, 'clients':clients, 'Photo_Product':Photo_Product,
	 		'products': products, 'initial': initial, 'video': video, 'hows': hows,
	 		'how_text': how_text, 'ingredients': ingredients, 'product_prizes': product_prizes}
	return render(request, 'index.html', data)

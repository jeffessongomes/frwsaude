from django import forms
from apps.inicial.models import Doubt, Client, PhotoProdutoAfterBefore
from .models import Product, Ingredients, Contact, Initial, How_Use, How_Use_Text, Video_Description, ProductsPrize


class DoubtForm(forms.ModelForm):
  class Meta:
    model = Doubt
    fields = '__all__'
    widgets = {
      'ask': forms.TextInput(attrs={'class':'form-control', }),
      'response': forms.Textarea(attrs={'class':'form-control'}),
      
    }
    labels = {'ask': "Pergunta",
    		  'response': "Resposta",
    }


class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control', }),
      'details': forms.Textarea(attrs={'class':'form-control'}),
      
    }
    labels = {'name': "Nome",
    		  'details': "Detalhes",
    }

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control', }),
      'price': forms.NumberInput(attrs={'class':'form-control'}),
      'ingredients': forms.SelectMultiple(attrs={'class':'form-control', 'required':False}),
      'image': forms.FileInput(attrs={'class':'form-control'}),
      'details': forms.Textarea(attrs={'class':'form-control'})
    }
    labels = {'name': "Nome", 'price': "Preço", 'ingredients': "Ingredientes",
    		  'image': "Imagem", 'details': "Detalhes",
    }

class IngredientsForm(forms.ModelForm):
  class Meta:
    model = Ingredients
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control', }),
      }
    labels = {'name': "Nome",}

class CaseForm(forms.ModelForm):
  class Meta:
    model = PhotoProdutoAfterBefore
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control', }),
      'photo': forms.FileInput(attrs={'class':'form-control'})
      }
    labels = {'name': "Nome", 'photo': "Foto"}

class InitialForm(forms.ModelForm):
  class Meta:
    model = Initial
    fields = '__all__'
    widgets = {
      'title': forms.Textarea(attrs={'class':'form-control', }),
      'subtitle': forms.Textarea(attrs={'class':'form-control'})
      }
    labels = {'title': "Título", 'subtitle': "Subtítulo"}

class HowUseForm(forms.ModelForm):
  class Meta:
    model = How_Use
    fields = '__all__'
    widgets = {
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'details': forms.Textarea(attrs={'class':'form-control'}),
      'image': forms.FileInput(attrs={'class': 'form-control'}), 
      }
    labels = {'title': "Título", 'details': "Detalhes", 'image': "Imagem" }

class HowUseTextForm(forms.ModelForm):
  class Meta:
    model = How_Use_Text
    fields = '__all__'
    widgets = {
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'subtitle': forms.TextInput(attrs={'class':'form-control'}),
      'details': forms.Textarea(attrs={'class': 'form-control'}), 
      }
    labels = {'title': "Título", 'details': "Detalhes", 'subtitle': "Subtítulo" }

class VideoDescriptionForm(forms.ModelForm):
  class Meta:
    model = Video_Description
    fields = '__all__'
    widgets = {
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'details': forms.Textarea(attrs={'class':'form-control'}),
      'video': forms.FileInput(attrs={'class': 'form-control'}), 
      }
    labels = {'title': "Título", 'details': "Detalhes", 'video': "Video" }

class ProductPrizeForm(forms.ModelForm):
  class Meta:
    model = ProductsPrize
    fields = '__all__'
    widgets = {
    	'qnt': forms.TextInput(attrs={'class':'form-control'}),
    	'image': forms.FileInput(attrs={'class':'form-control'}),
    	'preco_one': forms.TextInput(attrs={'class':'form-control'}),
    	'por_div': forms.TextInput(attrs={'class':'form-control'}),
      	'prize_div': forms.TextInput(attrs={'class':'form-control'}),
      	'buy_link': forms.TextInput(attrs={'class':'form-control'}),
      }
    labels = {'qnt': "Quantidade", 'image': "Imagem", 'preco_one': "Preço Único", 
    		 'por_div': "Dividido por", 'prize_div': "Preço Dividido", 'buy_link': "Link da Compra"}

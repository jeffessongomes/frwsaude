from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from apps.inicial.models import Doubt, Client, PhotoProdutoAfterBefore
from .models import Product, Ingredients, Contact, Initial, How_Use, Video_Description, How_Use_Text, TecDashImages
from .models import ProductsPrize
from .forms import DoubtForm, ClientForm, ProductForm, IngredientsForm, CaseForm, VideoDescriptionForm
from .forms import InitialForm, HowUseForm, HowUseTextForm, ProductPrizeForm

from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from .tokens import account_activation_token

import json

@login_required(login_url='login')
def index(request):
  option = TecDashImages.objects.all()

  context = {
    'option': option
  }

  return render(request, 'dashboard/dashboard.html', context)

def verifify_user(email, password):
  try:
    user = User.objects.get(email=email)
  except User.DoesNotExist:
    user = None
    
  if user is not None:
    user = authenticate(username=user.username, password=password)
    return user
  else:
    return user

def do_login(request):
  
  if request.method == 'POST':
    email = request.POST['email']; 
    password = request.POST['password'];
    user = verifify_user(email, password) 
        
    if user is not None:
      login(request, user)
      return redirect('index')
    else:
      error = True
      return render(request, 'dashboard/telaLogin.html', {'error': error})

  return render(request, 'dashboard/telaLogin.html')

def do_logout(request):
  logout(request)
  return redirect('login')

def forget_password(request):
  if request.method == 'POST':
    try:
      user = User.objects.get(email=request.POST['email'])  
    except User.DoesNotExist:
      user = None
    
    if user != None:
      msg_html = render_to_string('dashboard/email.html', {
        'user': user,
        'token':account_activation_token.make_token(user)
      })
      connection = mail.get_connection()
      connection.open()

      email = mail.EmailMessage(
          'Suporte - RemixManiacs',
          msg_html,   
          'entrego.oficialdelivery@gmail.com', # 'from'
          [user.email,], # 'to'
          connection=connection
      )

      email.send()
      confirmEmail = True
      return render(request, 'dashboard/forget-pass.html', {'confirmEmail': confirmEmail})
    else:
      error = True
      return render(request, 'dashboard/forget-pass.html', {'error': error})
      
  else:
    return render(request, 'dashboard/forget-pass.html')

def confirme_password(request, pk, token):
  try:
    user = User.objects.get(pk=pk)  
  except User.DoesNotExist:
    user = None
  
  if user != None:
    
    if account_activation_token.check_token(user, token):
      return render(request, 'dashboard/change-password.html', {'user_status':user})
    else:
      return HttpResponse("<h1 align='center'>Token does not exist</h1></br></br><a align='center' href='login'>click here</a>")
  else:
    return HttpResponse("<h1 align='center'>User does not exist</h1></br></br><a align='center' href='forget_password'>click here</a>")


def change_password(request):
  if request.method == 'POST':
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
      user_status = request.POST['user_status']
      
      try:
        user = User.objects.get(pk=user_status)
      except User.DoesNotExist:
        user = None
      except ValueError:
        user = None

      if user != None:
        user.set_password(password1)
        user.save()

        return redirect('login')
      else:
        return HttpResponse("<h1 align='center'>Please, use the link of your email</h1>")        

    else:
      error = True
      return render(request, 'dashboard/change-password.html', {'error':error})

  error = False
  return render(request, 'dashboard/change-password.html', {'error':error})

# client doubt
@login_required(login_url='login')
def add_doubt(request):
  data = {}
  if request.method == 'POST':
    form = DoubtForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_doubt')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = DoubtForm()
  data['form'] = form
  return render(request, 'dashboard/doubt/add-doubt.html', data)

@login_required(login_url='login')
def list_doubt(request):
  data = {}
  doubts = Doubt.objects.all()
  data['doubts'] = doubts
  return render(request, 'dashboard/doubt/list-doubt.html', data)

@login_required(login_url='login')
def edit_doubt(request, pk):
  data = {}
  doubt = Doubt.objects.get(pk=pk)
  
  if request.method == 'POST':
    form = DoubtForm(data=request.POST, instance=doubt)
    if form.is_valid():
      form.save()
      
      return redirect('index')
    else:
      
      HttpResponse(json.dumps(form.errors))
  else:
    form = DoubtForm(instance=doubt)

  data['form'] = form; data['doubt'] = doubt;

  return render(request, 'dashboard/doubt/edit-doubt.html', data)

@login_required(login_url='login')
def delete_doubt(request, pk):
  doubt = Doubt.objects.get(pk=pk)
  doubt.delete()
  return redirect('list_doubt')


# crud client
@login_required(login_url='login')
def add_client(request):
  data = {}
  if request.method == 'POST':
    form = ClientForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_client')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = ClientForm()
  data['form'] = form

  return render(request, 'dashboard/client/add-client.html', data)

@login_required(login_url='login')
def list_client(request):
  data = {}
  clients = Client.objects.all()
  data['clients'] = clients
  return render(request, 'dashboard/client/list-client.html', data)

@login_required(login_url='login')
def edit_client(request, pk):
  data = {}
  client = Client.objects.get(pk=pk)
  
  if request.method == 'POST':
    form = ClientForm(data=request.POST, instance=client)
    if form.is_valid():
      form.save()
      
      return redirect('index')
    else:
      
      HttpResponse(json.dumps(form.errors))
  else:
    form = ClientForm(instance=client)

  data['form'] = form; data['client'] = client;

  return render(request, 'dashboard/client/edit-client.html', data)

@login_required(login_url='login')
def delete_client(request, pk):
  client = Client.objects.get(pk=pk)
  client.delete()
  return redirect('index')


# crud product
@login_required(login_url='login')
def add_product(request):
  data = {}
  if request.method == 'POST':
    form = ProductForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_product')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = ProductForm()
  data['form'] = form

  return render(request, 'dashboard/product/add-product.html', data)

@login_required(login_url='login')
def list_product(request):
  data = {}
  products = Product.objects.all()
  data['products'] = products
  return render(request, 'dashboard/product/list-product.html', data)

@login_required(login_url='login')
def edit_product(request, pk):
  data = {}
  product = Product.objects.get(pk=pk)
  
  if request.method == 'POST':
    product.image.delete()
    form = ProductForm(data=request.POST, files=request.FILES, instance=product)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      
      HttpResponse(json.dumps(form.errors))
  else:
    form = ProductForm(instance=product)

  data['form'] = form; data['product'] = product;

  return render(request, 'dashboard/product/edit-product.html', data)

@login_required(login_url='login')
def delete_product(request, pk):
  product = Product.objects.get(pk=pk)
  product.delete()
  return redirect('index')


# crud ingredient
@login_required(login_url='login')
def add_ingredients(request):
  data = {}
  if request.method == 'POST':
    form = IngredientsForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_ingredients')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = IngredientsForm()
  data['form'] = form

  return render(request, 'dashboard/ingredient/add-ingredient.html', data)

@login_required(login_url='login')
def list_ingredients(request):
  data = {}
  ingredients = Ingredients.objects.all()
  data['ingredients'] = ingredients
  return render(request, 'dashboard/ingredient/list-ingredient.html', data)

@login_required(login_url='login')
def edit_ingredients(request, pk):
  data = {}
  ingredient = Ingredients.objects.get(pk=pk)
  
  if request.method == 'POST':
    form = IngredientsForm(data=request.POST, instance=ingredient)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      
      HttpResponse(json.dumps(form.errors))
  else:
    form = IngredientsForm(instance=ingredient)

  data['form'] = form; data['ingredient'] = ingredient;

  return render(request, 'dashboard/ingredient/edit-ingredient.html', data)

@login_required(login_url='login')
def delete_ingredients(request, pk):
  ingredient = Ingredients.objects.get(pk=pk)
  ingredient.delete()
  return redirect('index')


# crud cases
@login_required(login_url='login')
def add_case(request):
  data = {}
  if request.method == 'POST':
    form = CaseForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_case')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = CaseForm()
  data['form'] = form

  return render(request, 'dashboard/case/add_case.html', data)

@login_required(login_url='login')
def list_case(request):
  data = {}
  cases = PhotoProdutoAfterBefore.objects.all()
  data['cases'] = cases
  return render(request, 'dashboard/case/list-case.html', data)

@login_required(login_url='login')
def edit_case(request, pk):
  data = {}
  case = PhotoProdutoAfterBefore.objects.get(pk=pk)
  
  if request.method == 'POST':
    case.photo.delete()
    
    form = CaseForm(data=request.POST, files=request.FILES, instance=case)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      
      HttpResponse(json.dumps(form.errors))
  else:
    form = CaseForm(instance=case)

  data['form'] = form; data['case'] = case;

  return render(request, 'dashboard/case/edit-case.html', data)

@login_required(login_url='login')
def delete_case(request, pk):
  case = PhotoProdutoAfterBefore.objects.get(pk=pk)
  case.delete()
  return redirect('index')


# crud initial
@login_required(login_url='login')
def edit_initial(request):
  data = {}
  initial = Initial.objects.get(pk=1)
  
  if request.method == 'POST':
    form = InitialForm(data=request.POST, instance=initial)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      
     HttpResponse(json.dumps(form.errors))
  else:
    form = InitialForm(instance=initial)

  data['form'] = form; data['initial'] = initial;

  return render(request, 'dashboard/initial/edit-initial.html', data)

# crud How Use
@login_required(login_url='login')
def add_how(request):
  data = {}
  if request.method == 'POST':
    form = HowUseForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_how')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = HowUseForm()
  data['form'] = form

  return render(request, 'dashboard/how/add-how.html', data)

@login_required(login_url='login')
def list_how(request):
  data = {}
  hows = How_Use.objects.all()
  data['hows'] = hows
  return render(request, 'dashboard/how/list-how.html', data)

@login_required(login_url='login')
def edit_how(request, pk):
  data = {}
  how = How_Use.objects.get(pk=pk)
  
  if request.method == 'POST':
    how.image.delete()
    form = HowUseForm(data=request.POST, files=request.FILES, instance=how)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      
     HttpResponse(json.dumps(form.errors))
  else:
    form = HowUseForm(instance=how)

  data['form'] = form; data['how'] = how;

  return render(request, 'dashboard/how/edit-how.html', data)

@login_required(login_url='login')
def delete_how(request, pk):
  how = How_Use.objects.get(pk=pk)
  how.delete()
  return redirect('index')

# crud how text
@login_required(login_url='login')
def edit_how_text(request):
  data = {}
  how = How_Use_Text.objects.get(pk=1)
  
  if request.method == 'POST':
    form = HowUseTextForm(data=request.POST, instance=how)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      
     HttpResponse(json.dumps(form.errors))
  else:
    form = HowUseTextForm(instance=how)

  data['form'] = form; data['how'] = how;

  return render(request, 'dashboard/how_text/edit-how-text.html', data)


# crud how text
@login_required(login_url='login')
def edit_video_description(request):
  data = {}
  video = Video_Description.objects.get(pk=1)
  
  if request.method == 'POST':
    form = VideoDescriptionForm(data=request.POST, files=request.FILES, instance=video)
    video.video.delete()
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      
     HttpResponse(json.dumps(form.errors))
  else:
    form = VideoDescriptionForm(instance=video)

  data['form'] = form; data['video'] = video;

  return render(request, 'dashboard/video_description/edit-video-description.html', data)


# crud product prize
@login_required(login_url='login')
def add_product_prize(request):
  data = {}
  if request.method == 'POST':
    form = ProductPrizeForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_product_prize')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = ProductPrizeForm()
  data['form'] = form

  return render(request, 'dashboard/product_prize/add_product_prize.html', data)

@login_required(login_url='login')
def list_product_prize(request):
  data = {}
  product_prize = ProductsPrize.objects.all()
  data['product_prize'] = product_prize
  return render(request, 'dashboard/product_prize/list_product_prize.html', data)

@login_required(login_url='login')
def edit_product_prize(request, pk):
  data = {}
  product_prize = ProductsPrize.objects.get(pk=pk)
  
  if request.method == 'POST':
    form = ProductPrizeForm(data=request.POST, files=request.FILES, instance=product_prize)
    product_prize.image.delete()
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      
     HttpResponse(json.dumps(form.errors))
  else:
    form = ProductPrizeForm(instance=product_prize)

  data['form'] = form; data['product_prize'] = product_prize;

  return render(request, 'dashboard/product_prize/edit_product_prize.html', data)

@login_required(login_url='login')
def delete_product_prize(request, pk):
  product_prize = ProductsPrize.objects.get(pk=pk)
  product_prize.image.delete()
  product_prize.delete()

  return redirect('index')
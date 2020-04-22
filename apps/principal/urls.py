from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name="index"),
   
   path('add_doubt', views.add_doubt, name="add_doubt"),
   path('edit_doubt/<int:pk>', views.edit_doubt, name="edit_doubt"),
   path('list_doubt', views.list_doubt, name="list_doubt"),
   path('delete_doubt/<int:pk>', views.delete_doubt, name="delete_doubt"),

   path('add_client', views.add_client, name="add_client"),
   path('edit_client/<int:pk>', views.edit_client, name="edit_client"),
   path('list_client', views.list_client, name="list_client"),
   path('delete_client/<int:pk>', views.delete_client, name="delete_client"),
   
   path('add_product', views.add_product, name="add_product"),
   path('edit_product/<int:pk>', views.edit_product, name="edit_product"),
   path('list_product', views.list_product, name="list_product"),
   path('delete_product/<int:pk>', views.delete_product, name="delete_product"),

   path('add_ingredients', views.add_ingredients, name="add_ingredients"),
   path('edit_ingredients/<int:pk>', views.edit_ingredients, name="edit_ingredients"),
   path('list_ingredients', views.list_ingredients, name="list_ingredients"),
   path('delete_ingredients/<int:pk>', views.delete_ingredients, name="delete_ingredients"),

   path('add_case', views.add_case, name="add_case"),
   path('edit_case/<int:pk>', views.edit_case, name="edit_case"),
   path('list_case', views.list_case, name="list_case"),
   path('delete_case/<int:pk>', views.delete_case, name="delete_case"),

   path('add_how', views.add_how, name="add_how"),
   path('edit_how/<int:pk>', views.edit_how, name="edit_how"),
   path('list_how', views.list_how, name="list_how"),
   path('delete_how/<int:pk>', views.delete_how, name="delete_how"),

   path('edit_initial', views.edit_initial, name="edit_initial"),

   path('edit_how_text', views.edit_how_text, name="edit_how_text"),

   path('edit_video_description', views.edit_video_description, name='edit_video_description'),

   path('login', views.do_login, name="login"),
   path('logout', views.do_logout, name="logout"),

   path('forget_password', views.forget_password, name='forget_password'),
   path('confirme_password/<int:pk>/<str:token>', views.confirme_password, name='confirme_password'),
   path('change_password', views.change_password, name='change_password'),

   path('add_product_prize', views.add_product_prize, name="add_product_prize"),
   path('edit_product_prize/<int:pk>', views.edit_product_prize, name="edit_product_prize"),
   path('list_product_prize', views.list_product_prize, name="list_product_prize"),
   path('delete_product_prize/<int:pk>', views.delete_product_prize, name="delete_product_prize"),

]
from . import views
from django.urls import path


app_name ='order'

urlpatterns = [
    path('display_order', views.make_order, name ='make_order'),
    
]

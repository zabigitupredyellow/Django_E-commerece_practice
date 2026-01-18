from django.urls import path
from . import views
urlpatterns = [
    path ('', views.index ,name = "shop"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('tracker/', views.tracker, name="tracker "),
    path('search/', views.search, name="search "),
    path('product/', views.product_view, name="product"),
    path('check/', views.checkout, name="check  "),
]
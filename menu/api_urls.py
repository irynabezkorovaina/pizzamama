from django.urls import path
from . import views

app_name = "menu"   # it's for the link in html file: <a href="{% url 'menu:index' %}">See our menu</a>

urlpatterns = [
    path('GetPizzas', views.api_get_pizza)
]

from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

# Our pizzas: Vegetarian, 4 cheeses, Chicken mushrooms, Meat lover


def index(request):
    pizzas = Pizza.objects.all().order_by('price')
    '''pizzas_names_and_price = [pizza.name + " : " + str(pizza.price) + "$" for pizza in pizzas]
    pizzas_names_and_price_str = ", ".join(pizzas_names_and_price)
    return HttpResponse("Our pizzas : " + pizzas_names_and_price_str)'''
    return render(request, 'menu/index.html', {'pizzas': pizzas})

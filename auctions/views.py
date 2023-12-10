from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#import json
#from django.http import JsonResponse

from .models import User, Restaurant, MenuItem
from .forms import RestaurantForm, MenuItemForm

def index(request):
    restaurants = Restaurant._meta.model.objects.all()
    
    return render(request, "auctions/index.html", {
        'restaurants': restaurants,
    })
    

def login_view(request, **kwargs):
    message = None

    if 'message' in kwargs:
        message = kwargs['message']

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html", {
            "message": message
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")   



def restaurant(request, restaurant_name):
    menu_items = Restaurant.objects.get(name=restaurant_name).menu_items.all()
    return render(request, "auctions/restaurant.html" , {
        'restaurant': restaurant_name,
        'menu_items': menu_items,
    })


def add_restaurant(request):
    if request.method == "GET":
        return render(request, "auctions/create_restaurant.html")
    elif request.method == "POST":
        restaurants = Restaurant.objects.create(
            name = request.POST["restaurant_name"],
        )
        restaurants.save()
        return redirect(index)



class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'auctions/index.html'
    context_object_name = 'restaurants'

    def get_context_data(self):
        c = super().get_context_data()
        return c
    
    def get_queryset(self):
        return Restaurant.objects.all()
    

def edit_menu_item(request, menu_item_id):
    menu_item = MenuItem.objects.get(id = menu_item_id)
    return render(request, "auctions/menu_item.html", {
        'menu_item': menu_item,
    })


def add_menu_item(request, restaurant_name):
    if request.method == "GET":
        return render(request, "auctions/create_menu_item.html", {
            'restaurant': restaurant_name,
        })
    elif request.method == "POST":
        menu_item = MenuItem.objects.filter(item_name=request.POST["item_name"]).all().values('pk')
        if not menu_item.exists():
            menu_item = MenuItem.objects.create(
                item_name = request.POST["item_name"],
                star_rating = request.POST["rating"],
                image = request.FILES.get('image', None),
                notes = request.POST["notes"],
            )
            restaurant = Restaurant.objects.get(name=restaurant_name)
            restaurant.menu_items.add(menu_item)
            menu_item.save()
            restaurant.save()
        else:
            request.method = "GET"
            return render(request, "auctions/create_menu_item.html", {
            'message': 'That item already exists.',
            'restaurant': restaurant_name,
        })
        return redirect('restaurant', restaurant_name)
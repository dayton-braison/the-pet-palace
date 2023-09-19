from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Pet, Category, CartItem, Order
from .forms import RegisterForm

def home(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    
    return render(request, "home.html", context)

def selected_pet_list(request, category_name):
    pet_list = Pet.objects.filter(category__name=category_name)
    context = {"category_name": category_name, "pet_list": pet_list}

    return render(request, "selected_pet_list.html", context)

def selected_pet(request, category_name, pet_name):
    user = request.user
    pet_details = Pet.objects.get(name=pet_name)
    cart_items = CartItem.objects.filter(user=user)
    context = {"pet_details": pet_details, "cart_items": cart_items}

    return render(request, "selected_pet.html", context)

def shopping_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    context = {"cart_items": cart_items}
    return render(request, "shopping_cart.html", context)

def add_to_cart(request, product_id):
    user = request.user
    product = Pet.objects.get(pk=product_id)

    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('shopping-cart')

def checkout(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        name = request.POST['name']
        card_number = request.POST['card_number']
        expiration = request.POST['expiration']
        cvv = request.POST['cvv']

        order = Order.objects.create(user=user, total_price=total_price, is_paid=True)

        cart_items.delete()
        messages.success(request, "Your order has been placed!!")
        return redirect("checkout-success")
        
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'checkout.html', context)

def checkout_success(request):
    return render(request, "checkout_success.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your account has been created!!")
            return redirect("home")
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect('home')
        else:
            messages.error(request, "Oops! There was an error while logging in. Please try again.")
            return redirect('login')
    else:
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out. Thanks for shopping at The Pet Palace!!")
    return redirect('login')
from django.shortcuts import render, redirect
from .forms import SignUpForm, ItemListForm, OrdersForm
from .models import Item, Orders, Profile

# Create your views here.
def index(request):
    items = Item.objects.all()

    context = {
        'items': items
    }

    return render(request, 'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def addItem(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = ItemListForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.listedBy = request.user
            item.save()
            return redirect('index')
    else:
        form = ItemListForm()
    context = {
        'form': form
    }
    return render(request, 'addItem.html', context)

def buyItem(request, id):
    item = Item.objects.get(id=id)
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.item = item
            order.user = request.user
            order.total = item.price * order.quantity
            order.save()
            return redirect('index')
    else:
        form = OrdersForm()

    context = {
        'item': item,
        'form': form
    }
    return render(request, 'buyItem.html', context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    orders = Orders.objects.filter(user=user).order_by('-orderedAt')
    profileUser, created = Profile.objects.get_or_create(user=user)

    context = {
        'orders': orders,
        'profileUser': profileUser
    }
    return render(request, 'profile.html', context)
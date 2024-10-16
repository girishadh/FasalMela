from django.shortcuts import render
from .forms import SignUpForm, ItemListForm

# Create your views here.
def index(request):
    return render(request, 'home.html')

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
    if request.method == 'POST':
        form = ItemListForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = ItemListForm()
    context = {
        'form': form
    }
    return render(request, 'addItem.html', context)

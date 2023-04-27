from django.shortcuts import render
from django.http import HttpResponse
from .models import Clothing
from .forms import ClothingFilterForm



def index(request):
    return render(request, 'index.html')



def clothing(request):
    clothing_list = Clothing.objects.all()

    # If the form has been submitted, filter the clothing_list queryset
    if request.GET:
        form = ClothingFilterForm(request.GET)
        if form.is_valid():
            sizes = form.cleaned_data['sizes']
            price_min = form.cleaned_data['price_min']
            price_max = form.cleaned_data['price_max']
            if sizes:
                clothing_list = clothing_list.filter(size__contains=sizes)
            if price_min:
                clothing_list = clothing_list.filter(price__gte=price_min)
            if price_max:
                clothing_list = clothing_list.filter(price__lte=price_max)
    else:
        form = ClothingFilterForm()

    return render(request, 'clothing.html', {'clothing_list': clothing_list, 'form': form})




def about(request):
    return render(request, 'О-нас.html')



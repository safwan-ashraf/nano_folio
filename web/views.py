import json
from django import forms
from django.shortcuts import render,redirect, get_object_or_404
from django.conf import settings
from django.http import response,JsonResponse
from django.http.response import HttpResponse
from web.models import Gallery,Category,Contact,About,Address
from web.forms import ContactForm


# Create your views here.
def index(request):
    galleries = Gallery.objects.all()
    categories = Category.objects.all()
    contacts = Contact.objects.all()
    abouts = About.objects.all()
    addresses = Address.objects.all()
    form = ContactForm()


    context={
        "galleries" : galleries,
        "categories" : categories,
        "contacts" : contacts,
        "abouts" : abouts,
        "addresses" : addresses,
        "MEDIA_URL" : settings.MEDIA_URL,
        "form" : form
    }
    return render(request,"index.html",context=context)


def category(request):
    category_name =request.GET.get('category')
    if category_name:
        if category_name == "All":
            projects = Gallery.objects.all().values()
            data = list(projects)  
            response_data = {
                "title" : "success",
                "data" : data,
            }
        elif Category.objects.filter(name=category_name).exists():
            if Gallery.objects.filter(category__name=category_name).exists():
                projects = Gallery.objects.filter(category__name=category_name).values()
                data = list(projects)  

                response_data = {
                    "title" : "success",
                    "data" : data,
                }
            else:
                response_data = {
                    "title" : "failed",
                    "message" : "projects not found",
                }
        else:
            response_data = {
                "title" : "failed",
                "message" : "Category not found",
            }
    else:
        response_data = {
            "title" : "failed",
            "message" : "Category not found",
        }

    return JsonResponse({'response_data': response_data})


def contact(request):
    form = ContactForm(request.POST)
    email = request.POST.get("email")
    if form.is_valid():
        if not Contact.objects.filter(email=email).exists():
            form.save()
            response_data = {
                "status" : "success",
                "title" : "Successfully registered",
                "message" : "You subscribed to our newsletter successfully."
            }
        else:
            response_data = {
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "Already subscribed"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "Already subscribed"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def product(request,pk):
    product = Gallery.objects.get(pk=pk)
    context = {
        "product" : product
    }
    return render(request,"product.html",context=context)	

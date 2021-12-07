from django.urls import path
from web.views import index,category,contact,product

app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("category/",category, name="category"),
    path("contact/", contact, name="contact"),
    path("product/<pk>/", product, name="product")
]
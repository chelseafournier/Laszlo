from django.conf.urls import url
from django.urls import path
from .views import homepage, laszlo, pictures, ambassador, contact

urlpatterns = [
    path('', homepage),
    path('laszlo/', laszlo, name="laszlo-view"),
    path('pictures/', pictures, name="pictures"),
    path('ambassador/', ambassador, name="ambassador"),
    path('contact/', contact, name="contact"),
]


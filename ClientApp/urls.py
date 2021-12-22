from django.urls import path, re_path
from ClientApp import views

from django.conf.urls.static import static
from django.conf import settings

from rest_framework.authtoken.models import Token

# token, created = Token.objects.create()

urlpatterns=[
    re_path(r'^client$', views.clientAPI),
    re_path(r'^client/([0-9])$', views.clientAPI),

    re_path(r'^bill$', views.billsAPI),
    re_path(r'^bill/([0-9]+)$', views.billsAPI),

    re_path(r'^product$', views.productsAPI),
    re_path(r'^product/([0-9]+)$', views.productsAPI),

    re_path(r'^bill_product$', views.Bills_ProductsAPI),
    re_path(r'^bill_product/([0-9]+)$', views.Bills_ProductsAPI),

    re_path(r'^client/loadfile', views.LoadFile),
    re_path(r'^login', views.Login.as_view(), name='login'),
    re_path(r'^', views.Index),

    re_path(r'^client/savefile$', views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
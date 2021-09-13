from django.shortcuts import render


# Create your views here.
def api_overview(request):
    api_urls = {
      'list':'/product-list/',
      'detail-view':'/product-detail/<int:id>/',
      'create':'/product-create/',
      'update':'product-update/<int:id>/',
      'delete': 'product-delete/<int:id>/'
    }
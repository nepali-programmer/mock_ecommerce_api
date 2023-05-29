from django.http import HttpResponseNotFound, HttpResponse
from product.models import Product

def pay_for_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        url = 'https://uat.esewa.com.np/epay/main'
        d = {
            'amt': product.amount,
            'pdc': 0,
            'psc': 0,
            'txAmt': 0,
            'tAmt': product.amount,
            'pid':product.pk,
            'scd':'EPAYTEST',
            'su':'',
            'fu':''
        }
        return HttpResponse('Successful')
    except Product.DoesNotExist:
        return HttpResponseNotFound('Product not available')
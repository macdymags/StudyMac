from django.http import HttpResponse
from django.template import loader
from.models import Shipment, Transit


def index(request):
    context = {
        'shipments': Shipment.objects.all(),
        'transits': Transit.objects.all()
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def shipment_detail(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    context = {
        'shipment': shipment,
        'transits': Transit.objects.filter(shipment=shipment)
    }
    template = loader.get_template('shipment_detail.html')
    return HttpResponse(template.render(context, request))


def transit_detail(request, pk):
    transit = Transit.objects.get(pk=pk)
    context = {
        'transit': transit
    }
    template = loader.get_template('transit_detail.html')
    return HttpResponse(template.render(context, request))
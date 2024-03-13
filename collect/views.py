from django.shortcuts import render


# Create your views here.
def collect(request):
    return render(request, 'collect/collection.html')


def collect_id(request):
    return render(request, 'collect/collection_id.html')

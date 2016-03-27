from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Species


@login_required
def generate_nursery_labels(request):
    if request.method == 'GET':
        pass
    responseData = {
        'species': list(Species.objects.all()),
    }
    return render(request, 'labels/generate_nursery_labels.html', responseData)



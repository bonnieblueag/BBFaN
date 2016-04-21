import os
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from labels.csv_generator import CSVGenerator
import labels.models as LabelModels
from django.conf import settings

@login_required
def get_label_entries_for_order(request, orderID):
    entries =  list(sorted(LabelModels.LabelEntry.objects.filter(order__id=orderID),
                           key=lambda entry: entry.cultivar.name))
    data = {'entries':[]}
    for e in entries:
        singleData = {
            'count': e.count,
            'cultivar': e.cultivar.name,
            'species': e.cultivar.species.name,
            'rootstock': e.rootstock.name,
        }
        data['entries'].append(singleData)
    return JsonResponse(data)


@login_required
def build_label_order(request):
    url = reverse("admin:labels_nurserylabelorder_add")
    return HttpResponseRedirect(url)



@login_required
def generate_nursery_labels(request):
    responseData = {'hidden_tag':'hidden=hidden'}
    if request.method == 'POST':

        data = request.POST
        order = LabelModels.NurseryLabelOrder.objects.filter(id=data['order']).first()
        if order:
            username = request.user.username
            outputDirectory = os.path.join(settings.MEDIA_ROOT, 'labels', username)
            if not os.path.exists(outputDirectory):
                os.makedirs(outputDirectory)
            front = os.path.join(outputDirectory, 'front.csv')
            back = os.path.join(outputDirectory, 'back.csv')
            generator = CSVGenerator()
            generator.generate_front(order, front)
            generator.generate_back(order, back)
            messages.add_message(request, messages.SUCCESS, 'CSVs generated')
            responseData['hidden_tag'] = ''
            responseData['frontLink'] = os.path.join(settings.MEDIA_URL, 'labels', username, 'front.csv')
            responseData['backLink'] = os.path.join(settings.MEDIA_URL, 'labels', username, 'back.csv')
        else:
            messages.add_message(request, messages.ERROR, 'Could not find order!')
    responseData['orders'] = list(LabelModels.NurseryLabelOrder.objects.filter(user=request.user))
    return render(request, 'labels/generate_nursery_labels.html', responseData)


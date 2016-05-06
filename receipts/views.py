from django.shortcuts import render
from bbfan.settings import RECEIPTS_MAIN_FOLDER


def add_receipts(request):
    data = {
        'receipts_directory': RECEIPTS_MAIN_FOLDER
    }
    return render(request, context=data, template_name='add_receipts.html')



def add_receipt(request):
    pass
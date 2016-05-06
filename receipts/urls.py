from django.conf.urls import url
import receipts.views as ReceiptViews


urls = [
    url(r'^receipts/receipt/add$', ReceiptViews.add_receipts, name='add_receipts'),
]


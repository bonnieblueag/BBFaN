from django.conf.urls import url
import labels.views as LabelViews


urls = [
    url(r'^nursery/generate/labels$', LabelViews.generate_nursery_labels, name='generate_nursery_labels'),
    url(r'^nursery/order/build', LabelViews.build_label_order, name='build_label_order'),
    url(r'^nursery/entries/order/(?P<orderID>\d+)$', LabelViews.get_label_entries_for_order, name='entries_for_order')
]


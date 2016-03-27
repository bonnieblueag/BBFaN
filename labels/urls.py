from django.conf.urls import url
import labels.views as LabelViews

urls = [
    url(r'^nursery/generate/labels$', LabelViews.generate_nursery_labels, name='generate_nursery_labels'),
]


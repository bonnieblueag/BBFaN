from django.conf.urls import include, url
from django.contrib import admin
from core import urls as CoreUrls
from core import views as CoreViews
from labels.urls import urls as LabelUrls

router = CoreUrls.router

urlpatterns = [
    # Examples:
    # url(r'^$', 'bbfan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', CoreViews.HomeView.as_view(), name='home'),
]

urlpatterns += LabelUrls

urlpatterns += [
    url(r'^api/', include(router.urls), name='api'),
    #url(r'^api/log_message', post_log_messages_json, name='log_message'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

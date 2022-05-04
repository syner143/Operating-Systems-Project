from django.conf.urls import url, include
from django.contrib import admin
from pharma import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pharma/', include('pharma.urls')),
    url(r'^$', views.home, name='index'),
]

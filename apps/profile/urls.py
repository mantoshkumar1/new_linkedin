from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.profile import views

app_name = 'profile'

urlpatterns = {
    path('', views.AccountView.as_view(), name='account'),
    url(r'^user/$', views.CreateUser.as_view(), name='create'),
    }

# The format_suffix_pattern allows us to specify the data format (raw json or
# even html) when we use the URLs. It appends the format to be used to every
# URL in the pattern.
urlpatterns = format_suffix_patterns(urlpatterns)

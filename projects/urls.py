from django.conf.urls import url
from . import views

urlpatterns=[
  url(r'^$',views.index, name='index'),
  url(r'^self/',views.self, name='self'),
  url(r'^project/',views.project, name='project'),
  url(r'^contact/',views.contact, name="contact"),
    

]
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^index/$',views.index,name="index"),
    url(r'^person/$',views.index,name="index"),
    url(r'^person/(?P<username>\w{0,50})/email/(?P<email>\w{0,50})$',views.singleUser,name="singleUser"),
    url(r'^update/',views.updatePerson,name="update"),
    url(r'^addPerson/',views.addPerson,name="addPerson"),
    url(r'^deletePerson/',views.deletePerson,name="delete")
]
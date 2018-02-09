from django.conf.urls import url
from . import views

app_name='RIS'
urlpatterns=[
	url(r'^$', views.RIS_Home,name='RIS_Home'),
	url(r'^Add_Res/$', views.Add_Res, name='Add_Res'),
	url(r'^View_Res/$', views.View_Res,name='View_Res'),
	url(r'^Edit_Res/$', views.Edit_Res,name='Edit_Res'),
	url(r'^Delete_Res/$', views.Delete_Res,name='Delete_Res'),
]
from django.urls import path

from . import views

app_name = 'forums'

urlpatterns = [
	path('', views.IndexView.as_view(),name = 'index'),
	path('f=<int:subforum_id>/',views.detailSubforum, name = 'sub_forum'),
	path('t=<int:thread_id>/',views.detailThread, name='thread'),
]
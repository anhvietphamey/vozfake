from django.urls import path

from . import views

app_name = 'forums'

urlpatterns = [
	path('', views.IndexView.as_view(),name = 'index'),
	path('f=<int:subforum_id>/',views.detailSubforum, name = 'sub_forum'),
	path('t=<int:thread_id>/',views.detailThread, name='thread'),
	#path('tinh-lich-tra-no-giam-dan',views.loanInfo, name = 'loan_info'),
	path('tinh-lich-tra-no-giam-dan',views.loanInfo_djangoForm, name = 'loaninfo_django'),
	path('lich-tra-no-chi-tiet/<int:start_principal>+<str:start_date_str>+<str:ir_str>+<int:periods>',views.repaymentSchedule, name = 'loan_repayment')
]
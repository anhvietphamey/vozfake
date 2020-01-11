from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

import numpy as np
import pandas as pd
from datetime import date

from .models import SubForum, Thread, Post
from .forms import LoanInfo
from .interest_module import loanRepayment
# Create your views here.

#MARK: Class-based views
class IndexView(generic.ListView):
	template_name = 'forums/index.html'
	context_object_name = 'subforum_list'
	
	def get_queryset(self):
		return SubForum.objects.all()

#MARK: Function-based views
def detailSubforum(request,subforum_id):
	subforum = get_object_or_404(SubForum,pk=subforum_id)
	#thread_list = Thread.objects.filter(parent=subforum).order_by('-created_on')
	context = {'subforum': subforum}
	return render(request,'forums/subforum.html',context)

def detailThread(request,thread_id):
	thread = Thread.objects.get(id = thread_id)
	context = {'thread': thread}
	thread.views +=1
	thread.save()
	return render(request,'forums/thread.html',context)	

# def loanInfo(request):
# 	template = loader.get_template('forums/loaninfo.html')
# 	return HttpResponse(template.render())

def loanInfo_djangoForm(request):
	if request.method == 'POST':
		loan_form = LoanInfo(request.POST)
		if loan_form.is_valid():
			start_principal = int(loan_form.cleaned_data['start_principal'].replace(",",""))
			start_date = loan_form.cleaned_data['start_date']
			ir = loan_form.cleaned_data['ir']/100
			periods = loan_form.cleaned_data['periods']			

			return HttpResponseRedirect(reverse('forums:loan_repayment',args=(start_principal,start_date,ir,periods)))

	else:
		loan_form = LoanInfo()
	
	return render(request,'forums/loaninfo_v2.html',{'loan_form':loan_form})

def repaymentSchedule(request,start_principal,start_date_str,ir_str,periods):
	#convert date string to type date
	start_date = date.fromisoformat(start_date_str)
	
	#convert interest rate string to type float
	ir = float(ir_str)
	schedule = loanRepayment(start_principal,start_date,ir,periods)

	#calculate variables for display purpose
	monthly_principal = int(start_principal/periods)
	total_interest = int(np.sum(schedule['Monthly interest']))
	total_payment = int(start_principal + total_interest)

	context = {
		'df':schedule,
		'start_principal':start_principal,
		'start_date':start_date,
		'periods':periods,
		'ir':round(ir*100,2),
		'monthly_principal':monthly_principal,
		'total_principal':start_principal,
		'total_interest':total_interest,
		'total_payment':total_payment
		}

	return render(request,'forums/repaymentschedule.html',context)

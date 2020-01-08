from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import SubForum, Thread, Post
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


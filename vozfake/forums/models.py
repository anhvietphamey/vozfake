from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SubForum(models.Model):
	sub_forum_name = models.CharField(max_length = 200)

	def __str__(self):
		return self.sub_forum_name


class Thread(models.Model):
	thread_name = models.CharField(max_length=200)
	thread_content = models.TextField()
	created_by = models.ForeignKey(User,on_delete=models.CASCADE) #delete thread if user is deleted
	created_on = models.DateTimeField('date created')
	parent = models.ForeignKey(SubForum, on_delete=models.PROTECT) #subforum cannot be deleted
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.thread_name

class Post(models.Model):
	posted_by = models.ForeignKey(User, on_delete=models.CASCADE) #delete post if user is deleted
	post_text = models.TextField()
	parent = models.ForeignKey(Thread,on_delete=models.CASCADE) #if thread is deleted, post will be deleted
	post_time = models.DateTimeField('date posted')
	
	def __str__(self):
		post_info = self.posted_by + self.post_time
		return post_info
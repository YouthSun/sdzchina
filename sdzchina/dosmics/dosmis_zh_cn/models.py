from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Learn(models.Model):
	part_en=models.CharField(max_length=45, null=True)
	part_describe_en=models.CharField(max_length=200, null=True)
	part_cn=models.CharField(max_length=45, null=True)
	part_describe_cn=models.CharField(max_length=200, null=True)
	part_de=models.CharField(max_length=45, null=True)
	part_describe_de=models.CharField(max_length=300, null=True)
	img=models.CharField(max_length=45, null=True)
	movie=models.CharField(max_length=45,null=True, default='')
	download=models.CharField(max_length=45, null=True)

class Edu(models.Model):
	book_cover=models.CharField(max_length=45,null=True)
	book_download=models.CharField(max_length=100,null=True)
	book_price=models.IntegerField(default=0)
	book_name=models.CharField(max_length=200,null=True,default='')

class Calendar(models.Model):
	schedule=models.CharField(max_length=45,null=True)
	daytime=models.CharField(max_length=5,null=True)
	width=models.IntegerField(default=0)
	color=models.CharField(max_length=45,null=True)

class Project(models.Model):
	projectName=models.CharField(max_length=45,null=True)
	support=models.CharField(max_length=200,null=True)
	projectDescribe=models.CharField(max_length=200,null=True)
	discussionLink=models.CharField(max_length=200,null=True)
	detailLink=models.CharField(max_length=200,null=True)

class University(models.Model):
	uni_name=models.CharField(max_length=45)

class Course(models.Model):
	uni_name=models.ForeignKey('University',on_delete=models.CASCADE)
	course_name=models.CharField(max_length=45,default='')

class Comments(models.Model):
	comment_question=models.CharField(max_length=450,default='')
	username=models.ForeignKey(User)
	views=models.IntegerField(default=0)
	replies=models.IntegerField(default=0)

class Comment_reply(models.Model):
	comment_text=models.CharField(max_length=450,default='')
	username=models.ForeignKey(User)
	comment_question=models.ForeignKey('Comments',on_delete=models.CASCADE)

class Project_detail(models.Model):
	project=models.ForeignKey('Project', on_delete=models.CASCADE)
	show_url=models.CharField(max_length=45,default='#')
	explain_url=models.CharField(max_length=45,default='#')
	download_url=models.CharField(max_length=45,default='#')
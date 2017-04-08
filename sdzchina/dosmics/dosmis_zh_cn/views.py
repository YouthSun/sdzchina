from django.shortcuts import render
from django.http import HttpResponse
from .models import Learn,Edu,Calendar,Project,University,Course,Comments, Project_detail
# Create your views here.

def index(request):
	return render(request, 'dosmis_zh_cn/index.html')

def products(request):
	templist=list()
	for i in range(0,4):
		templist.append(i)
	context={'list':templist}
	# add a model later, if needed.
	return render(request, 'dosmis_zh_cn/products.html',context)

def learn(request):
	templist=Learn.objects.order_by('id')
	context={'learn_models':templist}
	return render(request, 'dosmis_zh_cn/learn.html',context)

def edu(request):
	templist=Edu.objects.order_by('id')
	calendar=Calendar.objects.order_by('id')
	context={'Edu_models':templist,'Calendar_models':calendar}
	return render(request, 'dosmis_zh_cn/edu.html',context)

def projects(request):
	templist=Project.objects.order_by('id')
	context={'project_models':templist}
	return render(request, 'dosmis_zh_cn/projects.html',context)

def university(request):
	templist=University.objects.order_by('id')
	uni_course=list()
	for listItem in templist:
		courselist=Course.objects.filter(uni_name__uni_name=listItem.uni_name)
		uni_course.append({'uni_name':listItem.uni_name,'course_list':courselist})

	context={'uni_models':uni_course}
	return render(request, 'dosmis_zh_cn/about_the_uni.html',context)

def corporation(request):
	return render(request, 'dosmis_zh_cn/products-corporation.html')

def comments(request,community_model_id):
	return render(request, 'dosmis_zh_cn/comments_question.html')

def community(request):
	templist=Comments.objects.order_by('id')
	context={'community_models':templist}
	return render(request, 'dosmis_zh_cn/community.html', context)

def detail(request,project_detail_id):
	detaillist=Project_detail.objects.filter(project_id__id=project_detail_id)

	context={'detail_models':detaillist}
	return render(request, 'dosmis_zh_cn/project-detail.html',context)
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^products/$', views.products, name="products"),
	url(r'^learn/$', views.learn, name="learn"),
	url(r'^edu/$', views.edu, name="edu"),
	url(r'^projects/$', views.projects, name="projects"),
	url(r'^about_the_uni/$', views.university, name="university"),
	url(r'^products-corporation/$',views.corporation, name="corporation"),
	url(r'^projects/(?P<community_model_id>[0-9]+)$',views.comments,name="comments"),
	url(r'^community/',views.community,name="community"),
	url(r'^project_detail/(?P<project_detail_id>[0-9]+)$',views.detail,name="detail"),
]
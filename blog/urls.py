from django.conf.urls import url
from blog import views

urlpatterns = [
    


    url(r'^$', views.index, name="index" ),
    url(r'^view-post/(?P<pk>\d+)$', views.view_post, name="view-post"),
    url(r'^create-post/$', views.create_post, name="create-post"),
    url(r'^edit-post/(?P<pk>\d+)$', views.edit_post, name="edit-post"),
    url(r'^delete-post/(?P<pk>\d+)$', views.delete_post, name="delete-post"),
    url(r'^mis-post/$', views.mis_post, name="mi-post"),
]
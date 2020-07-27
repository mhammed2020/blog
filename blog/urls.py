from django.urls import path

from .import views
app_name='blog'

urlpatterns = [
    path('',views.allPosts,name='allPosts'),
    path('<int:id>/',views.detailPost,name='detailPost'),
    # url(r'^create$', views.create_post, name='create_post'),
    # url(r'^(?P<id>\d+)/edit$', views.editPost, name='edit_post'),

]
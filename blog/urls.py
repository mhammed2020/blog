from django.urls import path

from .import views
app_name='blog'

urlpatterns = [
    path('',views.allPosts,name='allPosts'),
    path('<int:id>/',views.detailPost,name='post'),
    path('create', views.create_post, name='create_post'),
    path('<int:id>/edit/', views.editPost, name='edit_post'),

]
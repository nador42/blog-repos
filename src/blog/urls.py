from django.urls import path

from .views import blog_posts, blog_post, index

urlpatterns=[
    path('',blog_posts,name="blog-blog_posts"),
    path('<int:pk>/',blog_post,name="blog-blog_post"),
    path('ind/',index,name="index")



]
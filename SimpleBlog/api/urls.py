from django.urls import path
from . import views

urlpatterns = [
    path('',views.ViewList.as_view(), name='post_list'),
    path('add',views.AddPost.as_view(),name='Add_List'),
    path('details/<str:pk>',views.PostDetails.as_view(), name='post_details'),
    path('detail/<str:pk>',views.PostDetail.as_view(), name='post_detail'),
    path('about/', views.AboutDetail.as_view(), name='about')
]
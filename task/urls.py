from django.urls import path
from .views import *


app_name = "task"
urlpatterns = [
    path('', list_view, name="list"),
    path('new/', create_view, name="create"),
    path('<str:task_id>/', detail_view, name="detail"),
    path('edit/<str:task_id>/', edit_view, name="edit"),
    path('delete/<str:task_id>/', delete_view, name="delete"),
    path('add_comment/<str:task_id>/<str:user_id>/', comment_add_view, name="add_comment"),
    path('edit_comment/<str:task_id>/<str:user_id>/<str:comment_id>/', comment_edit_view, name="edit_comment"),
    path('delete_comment/<str:task_id>/<str:user_id>/<str:comment_id>/', comment_delete_view, name="delete_comment"),
]


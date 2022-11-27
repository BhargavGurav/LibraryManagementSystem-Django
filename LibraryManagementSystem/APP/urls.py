from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', include('django.contrib.auth.urls')),
    path('backend/', views.backend, name="backend"),
    path('add/', views.add_student, name="add_student"),
    path('entry_book/', views.add_entry, name="addEntry"),
    path('del_entry/<str:entry_id>', views.del_entry, name='del_entry'),
    path('edit/<str:requested_id>', views.edit_student, name="edit"),
    path('delete_student/<str:request_id>', views.delete_student, name='delete_student'),
    path('entries/', views.entry, name="entry"),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.userpage),
    path('view_emp',views.view_emp,name='view_emp'),
    path('edit',views.edit,name='edit'),
    path('<int:emp_id>/edit',views.edit,name='edit'),
    path('<int:emp_id>/delete',views.delete,name='delete')
]
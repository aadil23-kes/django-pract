from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('all_emp',views.all_emp,name='all_emp'),
    path('add_emp',views.add_emp,name='add_emp')

]




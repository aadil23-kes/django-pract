from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('all_emp',views.all_emp,name='all_emp')

]




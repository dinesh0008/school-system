from django.urls import path
from login_management import views

app_name='login_management'

urlpatterns =[
    path('',views.index,name="index"),
]
from django.urls import path
from registration_management import views

app_name='registration_management'

urlpatterns =[
    path('',views.index,name="index"),
]

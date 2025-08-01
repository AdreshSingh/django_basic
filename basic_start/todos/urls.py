from django.urls import path

# ! adding views/pages

from .views import home,addtodos

urlpatterns=[
    path('',home,name="homepage"),
    path('add',addtodos,name="New Todo")
]
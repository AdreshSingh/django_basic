from django.urls import path

# ! adding views/pages

from .views import home,addtodos,detail,deletetodo,updatetodo

urlpatterns=[
    path('',home,name="homepage"),
    path('add',addtodos,name="New Todo"),
    path("details/<int:id>/",detail,name="details"),
    path("delete/<int:id>/",deletetodo,name="deletetodo"),
    path("update/<int:id>",updatetodo,name="updatetodo")
]
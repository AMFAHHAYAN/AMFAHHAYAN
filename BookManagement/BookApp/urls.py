from django.urls import path
from .views import *

urlpatterns = [
    path('',Create.as_view(),name="create"),
    path('list/',List.as_view(),name="list"),
    path('update/<int:id>',BookUpdate.as_view(),name="update"),
    path('delete/<int:id>',deletebook.as_view(),name="delete"),

]
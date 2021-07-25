from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('eleve', views.user_articles, name="eleve"),
    path('ajouter-eleve', views.AddArticle.as_view(), name="ajouter-eleve"),
    path('update-eleve/<int:pk>', views.UpdateArticle.as_view(), name="update-eleve"),
    path('delete-eleve/<int:pk>', views.DeleteArticle.as_view(), name="delete-eleve"),
]

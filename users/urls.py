from django.urls import path
from . import views
from users.views import GetPost, GetPutDelete

urlpatterns = [
    path('', GetPost.as_view()),
    path('<int:pk>/', GetPutDelete.as_view()),
]
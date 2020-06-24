from django.urls import path
from . import views
from users.views import GetPost, GetPutDelete

# below are the urls of users, to see urls of the project please go cmacgmAssignment.utls (there i included below urls).
urlpatterns = [
    path('', GetPost.as_view()),
    path('<int:pk>/', GetPutDelete.as_view()),
]

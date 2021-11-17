from .views import User_view
from django.urls import path

urlpatterns = [
    path('usr/',User_view.as_view()),
    path('usr/<int:id>/', User_view.as_view())


]
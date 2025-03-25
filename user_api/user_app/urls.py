from django.urls import path
from .views import CreateUserView, GetAllUsersView, GetUserView, UpdateUserView, DeleteUserView

urlpatterns = [
    path('users/', CreateUserView.as_view()),
    path('users/all/', GetAllUsersView.as_view()),
    path('users/<int:pk>/', GetUserView.as_view()),
    path('users/<int:pk>/update/', UpdateUserView.as_view()),
    path('users/<int:pk>/delete/', DeleteUserView.as_view()),
]

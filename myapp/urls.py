
from django.urls import path
from .views import CreateUser, UpdateAndDelete

urlpatterns = [
    path('api/auth/create-api/', CreateUser.as_view(), name='createUser'),
    path('api/auth/updateanddelete/<int:pk>/', UpdateAndDelete.as_view(), name='updateanddelete')
]
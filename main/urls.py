from django.urls import path
from main import views

urlpatterns = (
      path('', views.index, name="index"),
      path('delete/<int:pk>', views.delete, name="delete"),
      path('status/<int:pk>/<int:value>', views.status, name="status"),
)
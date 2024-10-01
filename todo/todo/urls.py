from django.urls import path

from .views import TodosAPIView, TodoAPIView, doneTodosAPIView

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),
    path('todo/<int:pk>/', TodoAPIView.as_view()),
    path('done/', doneTodosAPIView.as_view()),
]
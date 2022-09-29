from django.urls import path

from . import views


urlpatterns = [
    path('categorys/', views.CategoryListCreateAPIView.as_view()),
    path('categorys/<int:category_id>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('questions/', views.QuestionAnswerListCreateAPIView.as_view()),
    path('questions/<int:questions_id>/', views.QuestionAnswerRetrieveUpdateDestroyAPIView.as_view()),
]

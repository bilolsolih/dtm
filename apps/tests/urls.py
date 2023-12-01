from django.urls import path

from . import api_endpoints as views

app_name = 'tests'

urlpatterns = [
    path('test_category/list/', views.TestCategoryListAPIView.as_view(), name='test_category_list'),
    path('subject/list/', views.SubjectListAPIView.as_view(), name='subject_list'),
    path('topic/list/', views.TopicListAPIView.as_view(), name='topic_list'),
]

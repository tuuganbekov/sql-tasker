from django.urls import path
from sql.views import TestApiView, sql_task

urlpatterns = [
    path('', TestApiView.as_view(), name='test'),
    path('task/<int:pk>/', sql_task, name='sql'),
]

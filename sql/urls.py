from django.urls import path
from sql.views import TestApiView

urlpatterns = [
    path('', TestApiView.as_view(), name='test')
]

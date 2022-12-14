from django.urls import path
from .views import NewAccountView

urlpatterns=[
    path('newaccount/', NewAccountView.as_view(), name='newaccount')
]
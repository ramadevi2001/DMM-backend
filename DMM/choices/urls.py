# choices/urls.py

from django.urls import path
from .views import ChoiceListCreateView, ChoiceDetailView, UserChoicesView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('choices/', ChoiceListCreateView.as_view(), name='choice-list-create'),
    path('choices/<uuid:pk>/', ChoiceDetailView.as_view(), name='choice-detail'),
    path('choices/user/<int:user_id>/', UserChoicesView.as_view(), name='user-choices'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

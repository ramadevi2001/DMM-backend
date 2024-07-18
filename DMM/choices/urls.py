from django.urls import path
from .views import ChoiceListCreateView, ChoiceDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('choices/', ChoiceListCreateView.as_view(), name='choice-list-create'),
    path('choices/<int:user>/', ChoiceDetailView.as_view(), name='choice-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

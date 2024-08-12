from django.urls import path
from .views import ObservationListCreateView, ObservationDetailView

urlpatterns = [
    path('observations/', ObservationListCreateView.as_view(), name='observation-list-create'),
    path('observations/<uuid:pk>/', ObservationDetailView.as_view(), name='observation-detail'),
]

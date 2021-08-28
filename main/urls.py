from django.contrib import admin
from django.urls import path, include

from .views import CandidateListAPIView, CandidateDetailsAPIView

urlpatterns = [
    # path('rest-api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('candidates/', CandidateListAPIView.as_view(), name='candidates'),
    path('candidates/<int:pk>', CandidateDetailsAPIView.as_view(), name='candidate_details'),
]

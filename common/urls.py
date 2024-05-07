from django.urls import path
from .views import (ItemListAPIView, SponsorsListAPI, StudentListAPI, UniversityListAPI, StudentSponsorListAPI,
                    StatisticAPIView)

urlpatterns = [
    path('item-list/', ItemListAPIView.as_view()),
    path('sponsor/', SponsorsListAPI.as_view()),
    path('student/', StudentListAPI.as_view()),
    path('univer/', UniversityListAPI.as_view()),
    path('stsp/', StudentSponsorListAPI.as_view()),

    path("amount_sratistic/", StatisticAPIView.as_view())
]
from django.urls import path

from api.views.users import UserDetailView

urlpatterns = [
    path('users/me/', UserDetailView.as_view()),
]


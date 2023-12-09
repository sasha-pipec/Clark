from django.urls import path

from api.views.messages import MessageListCreateView
from api.views.users import UserDetailView
from api.views.channels import ChannelsListToUserView

urlpatterns = [
    path('users/me/', UserDetailView.as_view()),
    path('workspaces/<int:id>/channels/', ChannelsListToUserView.as_view()),

    path('messages/', MessageListCreateView.as_view())
]

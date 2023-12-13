from django.urls import path

from clark_app.views.channels import ChannelListCreateView, ChannelAddUserView, ChannelExitUserView
from clark_app.views.directs import DirectsAddUserView
from clark_app.views.pages import (MainPageView, AuthPageView, RegisterPageView,
                                   ConfirmEmailPageView, WorkspacePageView, WorkspaceDetailPageView)
from clark_app.views.users import (UserCreateView, UserConfirmEmailView, UserLoginView, logout_user)
from clark_app.views.workspaces import (WorkspaceCreateExitView, WorkspaceAddUserView, )

urlpatterns = [
    # Pages
    path('', MainPageView.as_view(), name='main'),
    path('auth/', AuthPageView.as_view(), name='auth'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('confirm_email/', ConfirmEmailPageView.as_view(), name='confirm'),
    path('workspaces/', WorkspacePageView.as_view(), name='workspace'),
    path('workspaces/<int:id>/', WorkspaceDetailPageView.as_view(), name='workspace_detail'),

    # Users
    path('users/', UserCreateView.as_view(), name='users'),
    path('users/auth/', UserLoginView.as_view(), name='users_auth'),
    path('users/logout/', logout_user, name='users_logout'),
    path('users/confirm_email/', UserConfirmEmailView.as_view(), name='users_confirm'),

    # Workspaces
    path('workspaces/create/', WorkspaceCreateExitView.as_view(), name='workspace_create'),
    path('workspaces/exit/', WorkspaceCreateExitView.as_view(), name='workspace_exit'),
    path('workspaces/<int:id>/invite/', WorkspaceAddUserView.as_view(), name='workspace_invite'),

    # Channels
    path('channels/<int:id>/add/', ChannelAddUserView.as_view(), name='channels_add_user'),
    path('channels/<int:id>/exit/', ChannelExitUserView.as_view(), name='channels_exit_user'),
    path('workspaces/<int:id>/channels/', ChannelListCreateView.as_view(), name='channels'),

    # Direct
    path('workspaces/<int:id>/directs/', DirectsAddUserView.as_view(), name='directs'),
]

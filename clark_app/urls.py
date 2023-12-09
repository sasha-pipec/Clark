from django.urls import path

from clark_app.views.pages import (MainPageView, AuthPageView, RegisterPageView,
                                   ConfirmEmailPageView, WorkspacePageView, WorkspaceDetailPageView)
from clark_app.views.users import (UserCreateView, UserConfirmEmailView, UserLoginView)
from clark_app.views.workspaces import (WorkspaceCreateView, )

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
    path('users/confirm_email/', UserConfirmEmailView.as_view(), name='users_confirm'),

    # Workspaces
    path('workspaces/create/', WorkspaceCreateView.as_view(), name='workspace_create'),
]

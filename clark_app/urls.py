from django.urls import path

from clark_app.views.pages import (MainPageView, AuthPageView, RegisterPageView,
                                   ConfirmEmailPageView, WorkspacePageView)
from clark_app.views.users import (UserCreateLoginView, UserConfirmEmailView)

urlpatterns = [
    # Pages
    path('', MainPageView.as_view(), name='main'),
    path('auth/', AuthPageView.as_view(), name='auth'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('confirm_email/', ConfirmEmailPageView.as_view(), name='confirm'),
    path('workspaces/', WorkspacePageView.as_view(), name='workspace'),

    # Users
    path('users/', UserCreateLoginView.as_view(), name='users'),
    path('users/confirm_email/', UserConfirmEmailView.as_view(), name='users_confirm'),
]

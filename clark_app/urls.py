from django.urls import path

from clark_app.views.main import (MainPageView, AuthPageView, RegisterPageView,
                                  ConfirmEmailPageView, WorkspacePageView)

urlpatterns = [
    # Pages
    path('', MainPageView.as_view(), name='main'),
    path('auth/', AuthPageView.as_view(), name='auth'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('confirm_email/', ConfirmEmailPageView.as_view(), name='confirm'),
    path('workspaces/', WorkspacePageView.as_view(), name='workspace'),
]

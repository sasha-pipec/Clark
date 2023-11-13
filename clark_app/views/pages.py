from django.shortcuts import render, redirect
from django.views import View


class MainPageView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('workspace')
        return render(request, 'clark_app/main.html')


class AuthPageView(View):

    def get(self, request):
        return render(request, 'clark_app/authorization.html')


class RegisterPageView(View):

    def get(self, request):
        return render(request, 'clark_app/registration.html')


class ConfirmEmailPageView(View):

    def get(self, request):
        return render(request, 'clark_app/confirm_email.html')


class WorkspacePageView(View):

    def get(self, request):
        return render(request, 'clark_app/workspaces.html')

from django.shortcuts import render
from django.views import View


class MainPageView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'clark_app/main.html')
        return render(request, 'clark_app/main.html')

from .forms import InputForm
from django.views import View
from .mixins import HelperClass
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
class FetchPrimeNumbers(View,HelperClass):
    def get(self, request):
        return render(request,'index.html')

    def post(self, request):
        form = InputForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data.get("input_number")
            response = self.get_prime(n)
            return JsonResponse({"success":response}, status=200)
        else:
            return JsonResponse(form.errors, status=400)
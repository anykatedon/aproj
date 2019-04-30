from django.shortcuts import render
from .forms import FeedbackForm, SearchDoctorForm
from .models import Doctor, Feedback
from django.db.models import Q


# Create your views here.
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'anapp/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'anapp/feedback_form.html', {'form': form})


def search_doctor(request):
    if request.method == 'POST':
        form = SearchDoctorForm(request.POST)

        if form.is_valid():
            pass

    else:
        form = SearchDoctorForm()

    return render(request, 'anapp/search_doctor.html', {'form': form})

def validate_doctorname(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            results = Feedback.objects.filter(Q(doctor__doctor_name__contains=q))
            print(results)
            return render(request, 'anapp/results.html', {'results': results})

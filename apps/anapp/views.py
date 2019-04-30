from django.shortcuts import render
from .forms import FeedbackForm


# Create your views here.
def feedback_form(request):
    if request.method == 'POST':
        form=FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'anapp/thanks.html')
    else:
        form=FeedbackForm()
    return render(request, 'anapp/feedback_form.html', {'form': form})

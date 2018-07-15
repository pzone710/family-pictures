from django.shortcuts import render
from first_app import forms


# Create your views here.
def welcome(request):
    my_dict = {'text': 'this is just a testing text, dont take it seriously'}
    return render(request, 'first_app/index.html', my_dict)

def form_request(request):
    form = forms.NewUserForm()

    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print('FILL UP SUCCESS')
            return welcome(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'first_app/signup.html', {'form': form})

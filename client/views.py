from django.shortcuts import render, redirect
from .forms import NameURLForm
from .models import NameURL

def name_url_form(request):
    if request.method == 'POST':
        form = NameURLForm(request.POST)
        if form.is_valid():
            # Extract the cleaned data from the form
            names = [
                form.cleaned_data['name1'],
                form.cleaned_data['name2'],
                form.cleaned_data['name3'],
                form.cleaned_data['name4'],
                form.cleaned_data['name5'],
                form.cleaned_data['name6'],
            ]
            urls = [
                form.cleaned_data['url1'],
                form.cleaned_data['url2'],
                form.cleaned_data['url3'],
                form.cleaned_data['url4'],
                form.cleaned_data['url5'],
            ]

            # Save names to the database
            for name in names:
                NameURL.objects.create(name=name)

            # Save URLs to the database (if provided)
            for url in urls:
                if url:
                    NameURL.objects.create(url=url)

            return redirect('success')  # Redirect to a success page
    else:
        form = NameURLForm()

    return render(request, 'name_url_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')


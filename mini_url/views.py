from django.shortcuts import render
from django.shortcuts import redirect,render, get_object_or_404
from mini_url.models import MiniURL
from mini_url.forms import MiniURLForm


def liste(request):
    minis = MiniURL.objects.order_by('-nb_acces')
    return render(request, "mini_url/liste.html", locals())


def nouveau(request):
    if request.method == "POST":
        form = MiniURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)
    else:
        form = MiniURLForm()

    return render(request, 'mini_url/nouveau.html', {form: form})


def redirection(request, code):
    mini = get_object_or_404(MiniURL, code=code)
    mini.nb_acces += 1
    mini.save()

    return redirect(mini.url, permanent=True)


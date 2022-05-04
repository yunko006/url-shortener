from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *

# TODO : 
    # moi je vais hash le lien : url_a_hash donc url_hashed = exemple
    # quand je vais écrire 127.0.0.1:8000/exemple je vais avoir un redirect vers le url_a_hash 
    # 2 trucs a faire : 
    # [ ]1-a la fonction de hash
    # [X]1-b ou bien faire la fonction qui permet de créer soit meme un nom : check si le nom existe pas
    # [X]/ 2- le redirect a partir de mon site

# redirect un url de facon définitive 

def home(request):

    return render(request, 'shorturl/home.html')


def choose_url(request):
    """ url_a_hash = "https://www.google.com/search?q=img&rlz=1C1VDKB_frFR982FR982&sxsrf=ALiCzsbsq5YHg4KLZuLzyFgjW59o8I7Y0A:1651263407896&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiRwO7Gi7r3AhVtzoUKHcZtCsIQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1"
    url_de_base = "127.0.0.1:8000/"
    url_hashed = "https://127.0.0.1:8000/image" 
    
    return redirect(url_hashed)"""

    if request.method != 'POST':
        form = ChooseURLNameForm()

    else:
        form = ChooseURLNameForm(data=request.POST)
        if form.is_valid():
            new_url = form.save(commit=False)
            # a rajouter : check si le nom n'est pas déja prit
            new_url.save()
            context= {"new_url": new_url}
            return render(request, 'shorturl/new_url.html', context)
 
    context= {"form": form}
    return render(request, 'shorturl/choose_url_name.html', context)


def hash_url(request):
    if request.method != 'POST':
        form = HashURLNameForm()

    else:
        form = HashURLNameForm(data=request.POST)
        if form.is_valid():
            new_url = form.save(commit=False)
            # TODO :hash l'url long avant de save 
            # save le tout
            new_url.save()
            context= {"new_url": new_url}
            return render(request, 'shorturl/new_url.html', context)
 
    context= {"form": form}
    return render(request, 'shorturl/hash_url.html', context)


def redirect_url(request, short):
    # check si short_url est dans la base de donnée si oui alors on redirect vers son url long else 404
    if get_object_or_404(URL, url_custom=short):
        long = URL.objects.get(url_custom=short)
        return redirect(long.url_long)

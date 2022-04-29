import re
from django.shortcuts import render, redirect

from .models import *
from .forms import *

# TODO : 
    # moi je vais hash le lien : url_a_hash donc url_hashed = exemple
    # quand je vais écrire 127.0.0.1:8000/exemple je vais avoir un redirect vers le url_a_hash 
    # 2 trucs a faire : 
    # 1-a la fonction de hash
    # 1-b ou bien faire la fonction qui permet de créer soit meme un nom : check si le nom existe pas
    # / 2- le redirect a partir de mon site

# redirect un url de facon définitive 

def home(request):

    return render(request, 'shorturl/home.html')


def choose_url(request):
    """ url_a_hash = "https://www.google.com/search?q=img&rlz=1C1VDKB_frFR982FR982&sxsrf=ALiCzsbsq5YHg4KLZuLzyFgjW59o8I7Y0A:1651263407896&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiRwO7Gi7r3AhVtzoUKHcZtCsIQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1"
    url_de_base = "127.0.0.1:8000/"
    url_hashed = "https://www.google.com/image" 
    
    return redirect('/some/url/')"""

    if request.method != 'POST':
        form = ChooseURLNameForm()

    else:
        form = ChooseURLNameForm(data=request.POST)
        if form.is_valid():
            new_url = form.save(commit=False)
            new_url.save()
            return render(request, 'shorturl/new_url.html')

    context= {"form": form}

    return render(request, 'shorturl/choose_url_name.html', context)
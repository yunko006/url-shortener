from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *

# TODO : 
    # moi je vais hash le lien : url_a_hash donc url_hashed = exemple
    # quand je vais écrire 127.0.0.1:8000/exemple je vais avoir un redirect vers le url_a_hash 
    # 2 trucs a faire : 
    # [X]1-a la fonction de hash
    # [X]1-b ou bien faire la fonction qui permet de créer soit meme un nom : check si le nom existe pas
    # [X]/ 2- le redirect a partir de mon site
    # [ ] html tableau pour voir tous les liens que j'ai crée
    # [ ] html pour delete un lien / edit

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
        # si il existe pas on crée
        if form.is_valid():
            new_url = form.save(commit=False)
            new_url.save()
            context= {"new_url": new_url}
            return render(request, 'shorturl/new_url.html', context)

        # si url long existe deja return l'url short qu'il y a dans la base de donnée
        else:
            # try block pour voir si l'url existe deja 
            try:
                url_used = form.data.get('url_long')
                custom_already_created = URL.objects.get(url_long=url_used)

                context = {
                    "custom_already_created": custom_already_created, 
                    "url_used": url_used
                }

                return render(request, 'shorturl/retrieve_url.html', context)
            # url n'existe pas dans la db
            except URL.DoesNotExist:
                pass


    context= {"form": form}
    return render(request, 'shorturl/choose_url_name.html', context)


def generate_url(request):
    if request.method != 'POST':
        form = HashURLNameForm()

    else:
        form = HashURLNameForm(data=request.POST)
        if form.is_valid():
            new_url = form.save(commit=False)
            # call la function create_short_url 
            generate_url = new_url.create_short_url()
            # asigne la variable au model 
            new_url.url_custom = generate_url
            # save dans le model
            new_url.save()
            context= {"new_url": new_url}
            return render(request, 'shorturl/new_url.html', context)

        else:
            # refractor car double utilisation de cette partie
            url_used = form.data.get('url_long')
            custom_already_created = URL.objects.get(url_long=url_used)

            context = {
                "custom_already_created": custom_already_created, 
                "url_used": url_used
            }

            return render(request, 'shorturl/retrieve_url.html', context)
            
 
    context= {"form": form}
    return render(request, 'shorturl/generate_url.html', context)


def redirect_url(request, short):
    # check si short_url est dans la base de donnée si oui alors on redirect vers son url long else 404
    if get_object_or_404(URL, url_custom=short):
        long = URL.objects.get(url_custom=short)
        return redirect(long.url_long)


def see_url(request):
    url_created = URL.objects.all()

    context = {"url_created": url_created}

    return render(request, 'shorturl/all_url.html', context)

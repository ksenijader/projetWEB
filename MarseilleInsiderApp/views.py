from django.shortcuts import render
from MarseilleInsiderApp.models import Loisir,Catégorie,Pack
from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def vw_home(request, ):
    title = "MARSEILLE INSIDER"
    description = "Explorez les meilleures activités à faire dans la magnifique ville de Marseille"
    button = "Voir les activités"
    block_description="Nos Activités Recommandées "
    button1="Voir les packs"
    return render(request, "home_page.html",
                  {"title": title, "description": description, "button": button, "block_description":block_description,"button1":button1,
                   "user":request.user})
def vw_activities(request, ):

    return render(request, "activities_page.html",
                  {"Loisirs":Loisir.objects.all(),"Categories":Catégorie.objects.all()})

def vw_packs(request,):

    return render(request, "packs_page.html", {"Pack":Pack.objects.all()})
def vw_activities_cat_filter(request, categorie):
    loisirs_list=Loisir.objects.filter(categorie=categorie)
    return render(request, "activities_cat_filter.html",{"Loisirs":loisirs_list,"Categories":Catégorie.objects.all()})

def vw_pack(request,id_pack):
   pack=Pack.objects.get(id_pack=id_pack)

   return render(request, "pack_page.html", {"pack":pack})
def vw_activity(request,id_loisir):
    loisir=Loisir.objects.get(id_loisir=id_loisir)
    return render(request, "activity_page.html", {"loisir":loisir})


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')  # Rediriger vers la page d'accueil après l'inscription
    else:
        form = InscriptionForm()

    return render(request, 'inscription_page.html', {'form': form})


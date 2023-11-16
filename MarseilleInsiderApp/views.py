from django.shortcuts import render
from MarseilleInsiderApp.models import Loisir,Catégorie
from django.shortcuts import render, redirect
from .forms import InscriptionForm

# Create your views here.

def vw_home(request, ):
    title = "MARSEILLE INSIDER"
    description = "Explorez les meilleures activités à faire dans la magnifique ville de Marseille"
    button = "Voir les activités"
    block_description="Nos Activités Recommandées "
    return render(request, "home_page.html",
                  {"title": title, "description": description, "button": button, "block_description":block_description})
def vw_activities(request, ):

    return render(request, "activitiesloop.html",
                  {"Loisirs":Loisir.objects.all(),"Categories":Catégorie.objects.all()})
def vw_activities_cat_filter(request, categorie):
    loisirs_list=Loisir.objects.filter(categorie=categorie)
    return render(request, "activitiesloop.html",{"Loisirs":loisirs_list,"Categories":Catégorie.objects.all()})

def vw_activity(request,id_loisir):
    loisir=Loisir.objects.get(id_loisir=id_loisir)
    return render(request,"activities.html",{"loisir":loisir})


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')  # Rediriger vers la page d'accueil après l'inscription
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', {'form': form})
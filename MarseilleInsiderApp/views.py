from django.shortcuts import render
from MarseilleInsiderApp.models import Loisir,Catégorie

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
def loop(request,categorie):
    loisirs_list=Loisir.objects.filter(categorie=categorie)
    return render(request,"activitiesloop.html",
                  {"Loisirs":loisirs_list})

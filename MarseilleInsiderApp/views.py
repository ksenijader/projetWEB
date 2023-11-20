from django.shortcuts import render
from MarseilleInsiderApp.models import Loisir,Catégorie,Pack,Client,AchetePack,AcheteLoisir
from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import ClientUpdateForm
from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm

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

def compte_client(request):
     client=Client.objects.get(nom_utilisateur=request.user.nom_utilisateur)
     achete_pack=AchetePack.objects.filter(id_client=request.user.id_client)
     achete_loisir=AcheteLoisir.objects.filter(id_client=request.user.id_client)
     return render(request,'compte_client.html',{"user":client,"achete_pack":achete_pack,"achete_loisir":achete_loisir})

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientUpdateForm
    template_name = 'client_update.html'
    success_url = reverse_lazy('compte')  # Replace with the URL where the user should be redirected after a successful update
    def get_object(self, queryset=None):
        return self.request.user

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/password_reset.html'  # Customize this template path


    def form_valid(self, form):
        # Custom logic to handle the password reset
        # This method is called when the form is successfully submitted
def vw_activity(request, id_loisir):
    loisir = Loisir.objects.get(pk=id_loisir)

    nombre_personnes = int(request.GET.get('nombre_participants', 1))

    prix_total = loisir.calcul_prix_total(nombre_personnes)

    context = {
        'loisir': loisir,
        'nombre_personnes': nombre_personnes,
        'prix_total': prix_total,
    }
    return render(request, 'activity_page.html', context)

def form_valid(self, form):
        # Custom logic to handle the password reset
        # This method is called when the form is successfully submitted
        # You can access the cleaned_data to get the form input
        username = form.cleaned_data['username']
        nouveau_mdp = form.cleaned_data['nouveau_mdp']
        confirmer_mdp = form.cleaned_data['confirmer_mdp']

        # Continue with the default behavior by calling the super method
        return super().form_valid(form)

    def get_success_url(self):
        # Customize the URL to redirect after a successful password reset
        return 'login'  # Customize this URL
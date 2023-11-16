from django.contrib import admin
from .models import Loisir
from .models import Pack
from .models import AcheteLoisir
from .models import AchetePack
from .models import Catégorie
from .models import Client
from .models import Prix
from .models import Fournisseur
from .models import Contient
# Register your models here.

admin.site.register(Loisir)
admin.site.register(Pack)
admin.site.register(AcheteLoisir)
admin.site.register(AchetePack)
admin.site.register(Catégorie)
admin.site.register(Fournisseur)
admin.site.register(Client)
admin.site.register(Prix)
admin.site.register(Contient)


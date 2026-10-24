from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from .models import Parrain, Filleul
from .exceptions import Parrain



def attribuer_parrain( filleul:Filleul ) -> BOOL:

    # Si le filleul a deja un parrain
    if filleul.parrain is not None:
        parrain = filleul.parrain
        raise ParrainExistantError(f"{filleul.nom} a deja un parrain : {parrain.nom}",parrain)
    else:
        # parrains_libre contient les parrains n'ayant pas de filleul
        parrains_libre = Parrain.objects.annotate(nb=Count("filleuls")).filter(nb=0).order_by("?")

        # si tout les parrains ont au moins un filleul
        if parrains_libre.count() != 0:
            parrains_libre = Parrain.objects.annotate(nb=Count("filleuls")).order_by("nb")
            filleul.parrain = parrains_libre[0]
            return filleul
        else:
            filleul.parrain = parrains_libre[0]
            return filleul


def parrainage_view(request):
        filleuls = Filleul.objects.filter(parrain=None)
        #si tout les filleuls ont des parraints
        if filleuls.count() == 0:
            message = "Tout les filleuls ont des parrains"
            return render(request, "", context={"message": message})
        else:
            #recuperation du premier filleul n'ayant pas de parrain
            filleul = filleuls[0]
            return render(request, "parrainage/parrainage.html", context={"filleul": filleul})

def parrainer(request, filleul_id):
    ...
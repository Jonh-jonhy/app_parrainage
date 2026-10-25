from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count

from .models import Parrain, Filleul
from .exceptions import ParrainageError, ParrainExistantError



def attribuer_parrain( filleul:Filleul ) -> Parrain:

    # Si le filleul a deja un parrain
    if filleul.parrain is not None:
        parrain = filleul.parrain
        raise ParrainExistantError(f"{filleul.nom} a deja un parrain : {parrain.nom}")
    else:
        # parrains_libre contient les parrains n'ayant pas de filleul
        parrains_libre = Parrain.objects.annotate(nb=Count("filleuls")).filter(nb=0).order_by("?")

        # si certains parrains n'ont pas encore de filleul
        if parrains_libre.count() != 0:
            filleul.parrain = parrains_libre[0]
            filleul.save()
            return filleul.parrain
            
        else:
        # si tout les parrains ont au moins un filleul
            parrains_libre = Parrain.objects.annotate(nb=Count("filleuls")).order_by("nb")
            filleul.parrain = parrains_libre[0]
            filleul.save()
            return filleul.parrain
            
def acceuil_view(request):
    return render(request, "parrainage/acceuil.html", context={})

def parrainage_view(request):
        filleuls = Filleul.objects.filter(parrain=None)
        #si tout les filleuls ont des parraints
        if filleuls.count() == 0:
            message = "Tout les filleuls ont des parrains"
            return render(request, "parrainage/termine.html", context={"message": message})
        else:
            #recuperation du premier filleul n'ayant pas de parrain
            filleul = filleuls[0]
            return render(request, "parrainage/parrainage.html", context={"filleul": filleul})

def parrainer(request, filleul_id):
    filleul = get_object_or_404(Filleul, pk=filleul_id)
    try:
        parrain = attribuer_parrain(filleul)
    except ParrainageError as e:
        message = str(e)
        context = {
            "error_message": message
        }
        return HttpResponse(message)
    else:
        context = {
            "filleul": filleul,
            "parrain": parrain
        }
        return render(request, "parrainage/parrainage.html", context)
    
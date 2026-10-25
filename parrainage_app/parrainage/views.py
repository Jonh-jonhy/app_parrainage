from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count

from .models import Parrain, Filleul
from .exceptions import ParrainageError, ParrainExistantError

# Generation pdf
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


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

def pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["content-Disposition"] = 'inline; filename="parrainage.pdf"'

    filleuls = Filleul.objects.select_related("parrain").order_by("nom")

    donnees = [["Filleul", "Parrain"]]
    for f in filleuls:
        parrain = f"{f.parrain.nom} {f.parrain.prenom}" if f.parrain else "-"
        donnees.append([f"{f.nom} {f.prenom}", parrain])

    tableau = Table(donnees, colWidths=[250, 250], repeatRows=1)
    tableau.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2b2e55")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f1f1f8")]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    #construction du document
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(response, pagesize=A4)
    doc.build([
        Paragraph("Liste du parrainage", styles["Title"]),
        Spacer(1, 20),
        tableau,
    ])

    return response

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
    
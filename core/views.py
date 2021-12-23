from django.shortcuts import render
import random

def home(request):
    return render(request,"core/home.html")


def password(request):

    password = ""

    # TODO --> Crear una lista de las letras del abecedario
    characters = list("abcdefghijklmnopqrstuvwxyz")

    # TODO --> Obtener el largo de la contraseña desde el formulario de home y guardarlo en una variable
    length = int(request.GET.get('length'))

    # TODO --> Obtener el valor del checkbox para mayusculas
    uppercase = request.GET.get('uppercase')

    if uppercase:
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
    if request.GET.get('special'):
        characters.extend(list("@#$%&*+-_!?"))

    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))


    # Recorrer la lista
    for i in range(length):

        password += random.choice(characters)
            

    return render(request,"core/password.html", {"password":password})



def about(request):
    return render(request,"core/about.html")

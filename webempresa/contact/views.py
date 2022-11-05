from django.shortcuts import render, redirect
from django.urls import reverse         # Se usa para direccionar templates por nombre
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request):
    # Se instancia el formulario ya que es una clase
    contact_form = ContactForm()

    if request.method == "POST":        # Se detecta que sea un formulario el que llame esta función
        contact_form = ContactForm(data=request.POST)   # Se recuperan los valores ingresados en el Formulario
        if contact_form.is_valid():
            # Si el formulario es válido, se guardan los valores
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Suponemos que todo ha ido bien
            # Se envía el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de Contacto",
                f"De {name} <{email}> \n\nEscribio:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["adroc65@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")   # Se le suma la cadena OK al GET para sensar que todo a ido bien
            except Exception:
                # Existe un error
                return redirect(reverse('contact')+"?fail")

    # Se inyecta el formulario a la vista
    return render(request, "contact/contact.html", {'form': contact_form})

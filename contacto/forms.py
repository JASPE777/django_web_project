from django import forms

class formulario_contacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True, max_length=60 )

    email=forms.CharField(label="Email", required=True)

    telefono=forms.IntegerField(label="Tel/Cel", required=True,)  

    mensaje=forms.CharField(label="Mensaje", widget=forms.Textarea )

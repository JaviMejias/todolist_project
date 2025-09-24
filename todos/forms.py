from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["name", "description", "due_date"]
        labels = {
            "name": "Nombre de la tarea",
            "description": "Descripción",
            "due_date": "Fecha de vencimiento",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Nombre de la tarea",
                "class": "w-full border border-gray-300 rounded-lg px-4 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 ease-in-out"
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Descripción",
                "class": "w-full border border-gray-300 rounded-lg px-4 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 ease-in-out"
            }),
            "due_date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type": "date",
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 mt-1"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['due_date'].required = False

        if self.instance and self.instance.due_date:
            self.initial['due_date'] = self.instance.due_date.strftime('%Y-%m-%d')

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        if not name.strip():
            raise forms.ValidationError("El nombre de la tarea no puede estar vacío.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        if not description.strip():
            raise forms.ValidationError("La descripción no puede estar vacía.")
        return description

    def clean_due_date(self):
        due_date = self.cleaned_data.get("due_date")
        if not due_date:
            raise forms.ValidationError("La fecha de vencimiento no puede estar vacía.")
        return due_date

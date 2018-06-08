from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from datetime import datetime,timedelta

class ReservaForm(forms.Form):
    inicio = forms.DateTimeField(
        label= 'Fecha Inicio',
        widget=DateTimePickerInput(
            options={
                    "format": "DD/MM/YYYY HH:mm", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": False,
                    "minDate": (datetime.now()+timedelta(hours=1)).strftime("%m/%d/%Y %H:%M"),
                })
    )
    fin = forms.DateTimeField(
        label= 'Fecha Fin',
        widget=DateTimePickerInput(
            options={
                "format": "DD/MM/YYYY HH:mm",  # moment date-time format
                "showClose": True,
                "showClear": True,
                "showTodayButton": False,
                "minDate": (datetime.now()+timedelta(hours=1)).strftime("%m/%d/%Y %H:%M"),
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get("inicio")
        fin = cleaned_data.get("fin")
        if inicio and fin:
            # Only do something if both fields are valid so far.
            if fin <= inicio:
                raise forms.ValidationError(
                    "La fecha final debe ser posterior a la inicial."
                )
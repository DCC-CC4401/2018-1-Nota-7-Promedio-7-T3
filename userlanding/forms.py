from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from datetime import datetime, timedelta


class BusquedaForm(forms.Form):
    fechaInicio = forms.DateTimeField(
        label= 'Fecha Inicio',
        widget=DateTimePickerInput(
            options={
                    "format": "DD/MM/YYYY HH:mm", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": False,
                    "defaultDate": (datetime.now()+timedelta(hours=1)).strftime("%m/%d/%Y %H:%M"),
                    "minDate": (datetime.now()+timedelta(hours=1)).strftime("%m/%d/%Y %H:%M"),
                    "sideBySide": True,
                    "daysOfWeekDisabled": [0,6],
                    "keepInvalid": True,
                })
    )
    fechaFin = forms.DateTimeField(
        label= 'Fecha Fin',
        widget=DateTimePickerInput(
            options={
                "format": "DD/MM/YYYY HH:mm",  # moment date-time format
                "showClose": True,
                "showClear": True,
                "showTodayButton": False,
                "defaultDate": (datetime.now() + timedelta(hours=1)+timedelta(minutes=30)).strftime("%m/%d/%Y %H:%M"),
                "minDate": (datetime.now() + timedelta(hours=1)+timedelta(minutes=30)).strftime("%m/%d/%Y %H:%M"),
                "sideBySide": True,
                "daysOfWeekDisabled": [0, 6],
                "keepInvalid": True,
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
            if inicio.hour < 9 or inicio.hour > 17:
                msg = "La hora de inicio debe estar entre las 9:00 y 18:00."
                self.add_error('inicio', msg)
            if fin.hour < 9 or (fin.hour == 18 and fin.minute > 0) or fin.hour > 18:
                msg = "La hora de fin debe estar entre las 9:00 y 18:00."
                self.add_error('fin', msg)

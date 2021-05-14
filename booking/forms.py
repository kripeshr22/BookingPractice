from django import forms

class AvailableForm(forms.Form):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KNG', 'KING'),
        ('QWN', 'QUEEN')
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True ,input_formats=["%Y-%m-%dT%H:%M",])
    check_out = forms.DateTimeField(required=True ,input_formats=["%Y-%m-%dT%H:%M",])

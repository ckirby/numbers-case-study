from django import forms

from humanize import errors

custom_error_messages = {
    "required": errors.ERRORS["POST"]["REQUIRED"],
    "invalid": errors.ERRORS["POST"]["INVALID"],
}


class NumberForm(forms.Form):
    number = forms.IntegerField(error_messages=custom_error_messages)

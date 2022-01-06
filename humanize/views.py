from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from humanize import errors
from humanize.forms import NumberForm
from humanize.utils import do_humanize


@require_http_methods(["GET", "POST"])
def humanize(request):
    if request.method == "GET":
        number = request.GET.get("number", None)
        if number is None:
            return JsonResponse(
                {"status": f"Error: {errors.ERRORS['GET']['REQUIRED']}"}
            )
        try:
            number = int(number)
        except ValueError:
            return JsonResponse({"status": f"Error: {errors.ERRORS['GET']['INVALID']}"})
    elif request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]
        else:
            return JsonResponse(
                {"status": f"Error: {form.errors.as_data()['number'][0].message}"}
            )

    return JsonResponse({"status": "ok", "num_in_english": do_humanize(number)})

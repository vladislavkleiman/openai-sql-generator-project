from django.http import JsonResponse


def health_check(request):
    # You might add checks for your database or other services here
    return JsonResponse({"status": "healthy"})
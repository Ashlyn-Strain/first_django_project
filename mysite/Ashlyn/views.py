from django.http import JsonResponse

# Create your views here.
def index(request):
    data = {
        "Name" : "Ashlyn Strain",
        "Track" : "Backend: Python",
        "Message" : "Thank you guys for this opportunity! I feel like I'm learning and understanding a lot!"
    }
    return JsonResponse(data)
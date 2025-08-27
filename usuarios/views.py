from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Área de administração de usuários")

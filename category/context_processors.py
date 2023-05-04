from .models import Category

def menu_links(request):
    links = Category.objects.all() #Consulta a la base de datos, tabla Categorias para que extraiga todos los objetos
    return dict(links=links)
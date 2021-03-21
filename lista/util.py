from .models import Item

def getItem():
    return Item.objects.all()

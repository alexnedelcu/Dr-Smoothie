from django.http import HttpResponse
from models import TestModel

def index(request):
    test = TestModel()
    test.name = "blah"
    test.save()
	
    result = ""
    for i in TestModel.objects.all():
       result = result + i.name + "<br>";
    return HttpResponse(result)


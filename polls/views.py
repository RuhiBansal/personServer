from django.http import HttpResponse, QueryDict
from polls.models import Person
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

#@csrf_exempt
def addPerson(request):
    method = request.method
    if method == 'POST':
        str = request.body.decode('utf-8')
        person = json.loads(str)

        name = person['name']
        birth = person['birth']
        death = person['death']
        p = Person(name=name, birthYear=birth, deathYear=death)
        #p.save()
        #return HttpResponse({'foo':'bar'})
        print person
        return JsonResponse(person)

def deletePerson(request):
    method = request.method
    if method == 'GET':
        id = request.GET['id']
        p = Person.objects.get(id=id)
        p.delete()
        return HttpResponse(json.dumps(p))

def updatePerson(request):
    method=request.method
    if method=='GET':
        id = request.GET['id']



@csrf_exempt
def index(request):
    print "index is calling new"
    print request.GET['name']
    name = request.GET['name']
    # print "query is ",request.GET['name']


    method = request.method
    if method == 'POST':
        print request.body.decode('utf-8')
        # body = json.loads(body_unicode)

    p = Person(name="abhay", birthYear=1993, deathYear=2000)
    # print p.validate_unique()
    # p.save()
    return HttpResponse(name)


def singleUser(request, username, email):
    print "user is ", username
    print "user is ", email
    return HttpResponse("params exmaple")


@csrf_exempt
def updatePerson(request):
    method = request.method
    if method == 'POST':
        print "yes"
    o = request.body.decode('utf-8')
    print(o)
    # return HttpResponse(request.body.decode('utf-8'))
    return HttpResponse(o)

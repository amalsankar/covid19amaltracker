from django.shortcuts import render
import requests


def home(request):

    return render(request,'home.html')
    

def index(request,cn):
    ab=request.POST['cn']

    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":ab}

    headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "f325d70ebcmsh684590eed4c5522p179fc6jsnc8cbfc9d8110"
            }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data=response['response']
    d=data[0]
    print(d)
    print(ab)
    context={
        'all':d['cases']['total'],'recovered':d['cases']['recovered'],'deaths':d['deaths']['total'],'new':d['cases']['new'],'critical':d['cases']['critical'],
        'ab':ab

    }


    return render(request,'index.html',context)

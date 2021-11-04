# from django.http import HttpResponse

# def home(request):
#     # print(request.GET.get('q'))
#     # print(request.COOKIES)
#     # print(request.path)
#     # print(request.method)
#     # print(request.user)//Login olmak gerekiyor hata almamak icin
#     html = "<html><body><h1>Hello World!</h1></body></html>"
#     return HttpResponse(html)


from django.shortcuts import render

def home(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2,3,4]
    }
    return render(request, 'app/home.html',context)

from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, JsonResponse

def index(request, id):
    people = ["Tim", "Bas", "Sad"]
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound("Загрузка страницы была завершена ошибкой")

def posts(request, id):
    return HttpResponse(f"Посты {id}")

def popular(request, id):
    return HttpResponse(f"Популярные посты {id}")

def last(request, id):
    return HttpResponse(f"Последние посты {id}")

def comments(request, id):
    return HttpResponse(f"Количество комментариев {id}")

def likes(request, id):
    return HttpResponse(f"Количество лайков {id}")

def user(request):
    login = request.GET.get("login", "ruz")
    password = request.GET.get("password", "12345")
    return HttpResponse(f"<h2>Логин: {login} Пароль: {password}</h2>")

def about(request):
    return HttpResponseRedirect("/about")

def contacts(request):
    return HttpResponsePermanentRedirect("/")

def access(request, login, password):
    if login == "admin" and password == "admin":
        return HttpResponse("Все норм")
    return HttpResponse(f"""
    <p>Log in: {login}</p>
    <p>Password: {password}</p>
    """)

def json(request):
    return JsonResponse(request.GET)

def set(request):
    key = request.GET.get("key", "none")
    value = request.GET.get("value", "none")
    response = HttpResponse(f"Привет {key} {value}")
    response.set_cookie(key, value)
    return response

def get(request):
    key = request.GET.get("key", "none")
    value = request.COOKIES[key]
    return HttpResponse(f"Пока {key} {value}")
    
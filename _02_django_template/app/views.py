from django.shortcuts import render
from django.utils import timezone

def index(request):
    return render(request, 'app/index.html')

def _template_context(request):
    """각 요청에 사용할 템플릿 실습 데이터를 만든다."""
    users = [
        {'id': 1234, 'name': 'Alice', 'age': 24, 'married': True},
        {'id': 2345, 'name': 'Bob', 'age': 34, 'married': False},
        {'id': 3456, 'name': 'Charlie', 'age': 25, 'married': True},
    ]

    return {
        'name': 'Django',
        'age': 13,
        'num': 1,
        'hobby': ['coding', 'reading', 'traveling'],
        'today': timezone.localtime(),
        'is_authenticated': True,
        'fruits': ['apple', 'banana', 'cherry'],
        'users': [] if request.GET.get('empty') == '1' else users,
    }


def variables_filters(request):
    return render(
        request,
        'app/01_variables_filters.html',
        _template_context(request),
    )

# 렌더링 전:  <p>My name is {{ name }}</p> (html)
# 렌더링 후: '<p>My name is' + context.name + '</p>' (python str)

def tags(request):
    return render(
        request,
        'app/02_tags.html',
        _template_context(request),
    )

def layout(request):
    return render(request, 'app/03_child.html')

def staticfiles(request):
    return render(request, 'app/04_staticfiles.html')

def urls(request):
    return render(request, 'app/05_urls.html')


def article(request, id: int):
    print(f'Article ID: {id}')

    return render(
        request,
        'app/05_urls.html',
        {'id': id},
    )


def search(request):
    print(request)
    print(request.GET)

    q = request.GET.get('q')
    lang = request.GET.get('lang')
    mode = request.GET.get('mode', 'view')

    return render(
        request,
        'app/05_urls.html',
        {'q': q, 'lang': lang, 'mode': mode},
    )

def bootstrap(request):
    return render(request, 'app/06_bootstrap.html')
from django.http import HttpResponse


def main(request):
    return HttpResponse("<h1>This will be the main page but you will be redirected to blogs for now</h1><a href='http://127.0.0.1:8000/blogs/'>Blogs</a>")
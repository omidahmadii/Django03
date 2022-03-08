from django.views.generic import ListView
from blog.models import Article, Category


class Home(ListView):
    context_object_name = 'articles'
    queryset = Article.objects.published()
    template_name = 'blog/home.html'

def detail(request):
    pass


def category(request):
    pass



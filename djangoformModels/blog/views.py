from django.shortcuts import render, redirect

from .forms import ArticleForm

from .models import Article

def index(request):
    articles = Article.objects.all().order_by('-dateTime')
    context = {
        'title':'Halaman Blog',
        'heading':'Halaman Daftar Blog',
        'articles': articles,
    }

    return render(request, 'blog.html', context)

def createArticle(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        else:
            form = ArticleForm()

    context = {
        'title':'Halaman Create Article',
        'heading':'Create Form Article',
        'form': form,
    }

    return render(request, 'createArticle.html', context)
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Blogspot',
        'hero':'Blog Saya',
        'developer':'Budi',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/contact','Contact'],
            # ['artikel/','Artikel'],
            # ['berita/','Berita'],
        ],
        'banner':'blog/images/blog.png'
    }
    return render(request, 'index.html', context)

# def artikel(request):
#     context = {
#         'title':'artikel',
#         'hero':'artikel Saya',
#         'developer':'asep',
#     }
#     return render(request, 'index.html', context)

# def berita(request):
#     context = {
#         'title':'berita',
#         'hero':'berita Saya',
#         'developer':'ucup',
#     }
#     return render(request, 'index.html', context)
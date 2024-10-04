from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Halaman Beranda</h1>")


def detail_arsip(request, kategori):
    headLine = "<h1>Detail Arsip</h1>"
    return HttpResponse(headLine + kategori)


def thn_arsip(request, tahun):
    headLine = "<h1>Tahun Arsip</h1>"
    thnArsip = "Tahun : " + tahun
    return HttpResponse(headLine + thnArsip)


def arsip(request, input):
    headLine = "<h1>Nomor Arsip</h1>"
    noArsip = input
    return HttpResponse(headLine + "Nomor %d" % noArsip)


# def tgl_arsip(request, tgl, bln, thn):
#     headLine = "<h1>Nomor Arsip</h1>"
#     tglArsip = tgl
#     blnArsip = bln
#     thnArsip = thn
#     return HttpResponse(headLine + "Tanggal : %d / %d / %d" % (tglArsip, blnArsip, thnArsip))


def tgl_arsip(request, **input):
    headLine = "<h1>Nomor Arsip</h1>"
    tglArsip = input['tgl']
    blnArsip = input['bln']
    thnArsip = input['thn']
    return HttpResponse(headLine + "Tanggal : %d / %d / %d" % (tglArsip, blnArsip, thnArsip))
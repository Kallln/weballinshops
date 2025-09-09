from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'judul' : 'WeBallin\' Shop',
        'creator' : 'Ahmad Haikal Najmuddin - PBP F',
        
    }

    return render(request, "main.html", context)
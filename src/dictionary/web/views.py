from django.shortcuts import render

from web.models import Word, Wordmeanig

def new(request):
    if request.method == "POST":
        word=request.POST.get("word")
        word_Meanings=request.POST.get("word_Meanings")
        new_word,create=Word.objects.get_or_create(word=word)
        print(new_word,create)
   
        Wordmeanig.objects.create(
            word=new_word,
            Wordmeanig=word_Meanings
        )

        # context={
        # "word":word,
        # "word_Meanings":word_Meanings,
        # }
        return render(request,"new.html")
    return render(request,"new.html")
    # if request.method == "POST":
    #     word_Meanings=request.POST.get("word_Meanings")
    #     context={
    #     "word_Meanings":word_Meanings
    #     }
    # return render(request,"new.html",context=context)
    
def index(request):
    if request.method == "POST":
        search_word=request.POST.get("search")
        word = Word.objects.filter(word=search_word)

        print(word)
        if word:
            meanings = Wordmeanig.objects.filter(word__in = word).order_by("priority")
            context = {
                'search':True,
                'missing':False,
                'meanings':meanings , 
                    
            }
            return render(request,"index.html",context)
        elif search_word == '':
            context={
                'search':''
            }
            return render(request,"index.html",context)
        else:
            meanings=f"{search_word}  not present in my Dictionary"
            context = {
                'search':True,
                'missing':True,
                'meanings':meanings ,     
            }
            return render(request,"index.html",context)
        
    else:
        context = {
            'search':True,
            'meanings':"",         
        }
        return render(request,"index.html",context)
            


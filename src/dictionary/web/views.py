from django.shortcuts import render


def index(request):
    dic = {'integers':'The whole numbers, plus their counterparts less than zero, and zero',
            'topic': 'a subject of conversation or discussion:',
            'website': 'a connected group of pages on the World Wide Web regarded as a single entity, usually maintained by one person or organization and devoted to a single topic or several closely related topics.',
            'signature': 'the act of signing a document.',
            'software':'Computers. the programs used to direct the operation of a computer, as well as documentation giving instructions on how to use them',
            'food':'any nourishing substance that is eaten, drunk, or otherwise taken into the body to sustain life, provide energy, promote growth, etc.'}
    
    if request.method == "POST":
        search=request.POST.get('search')
        if search == "":
            context = {
                'search':'',
                'word' : '',    
            }
            return render(request,"index.html",context)
        elif search in dic.keys():
            context = {
                'search':dic[search],
                'word' : search,  
            }

            return render(request,"index.html",context)
        else:
            context = {
                'search':'',
                'word' : '',    
            }
            return render(request,"index.html",context)
    else:
        context = {
            'search':"",
            'word' : "", 
               
        }
        return render(request,"index.html",context)
        


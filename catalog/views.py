from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='text-align:center'>Home Page</h1>")

from catalog.models import Book, Author, Genre


def index(request):
	num_books = Book.objects.all().count()
	num_authors = Author.objects.count()
	num_genre = Genre.objects.count()

	context = {
        'num_books': num_books,
        'num_authors': num_authors,        
        'num_genre': num_genre,
    }
	return render(request, 'index.html', context=context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Classes created for the forms challenge
class BookCreate(CreateView):
    model = Book
    fields = '__all__'


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'




class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')


################ AUTHOR VIEWS ################
class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')



################ GENRE VIEWS ################

def genreList(request):    
    genre = Genre.objects.all()
    return render(request, 'catalog/genre_list.html', context={'genre': genre})

def genreDetailView(request, pk):
    genre = Genre.objects.get(id=pk)
    return render(request, 'catalog/genre_detail.html', context={'genre': genre})

from catalog.forms import GenreForm
from django.shortcuts import redirect

def genreCreate(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            g_name = form.cleaned_data['name']
            p = Genre(name=g_name)
            p.save()
            return redirect('/catalog/genres')
    else:
        form = GenreForm()

    return render(request, 'catalog/genre_form.html', {'form': form})    


def genreUpdate(request, pk):
    genre = Genre.objects.get(id=pk)

    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre.name = form.cleaned_data['name']            
            genre.save()
            return redirect('/catalog/genre/'+ str(pk))
    else:
        form = GenreForm(initial={'name': genre.name})

    return render(request, 'catalog/genre_form.html', {'form': form})   

     

from django.contrib.auth.decorators import login_required

@login_required
def genreDelete(request, pk):
    genre = Genre.objects.get(id=pk)
    if request.method == 'POST':
        genre.delete()
        return redirect('/catalog/genres')
    return render(request, 'catalog/genre_delete.html', {'genre': genre})    



from catalog.forms import AuthorForm
def authorCreate(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']            
            last_name = form.cleaned_data['last_name']            
            date_of_birth = form.cleaned_data['date_of_birth']            
            date_of_death = form.cleaned_data['date_of_death']     
            author = Author(first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,date_of_death=date_of_death)       
            author.save()
            return redirect('/catalog/authors')
    else:
        form = AuthorForm()

    return render(request, 'catalog/author_form.html', {'form': form})    
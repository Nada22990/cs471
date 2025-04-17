from django.shortcuts import render
from .models import Book,Address,Student,Card11,Department11,Course11,Students11

from django.db.models import Q

# Create your views here.
from django.http import HttpResponse

from django.db.models import Count, Min, Max, Sum, Avg

def index(request): 
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html" , {"name": name})    #Change HttpResponse  to render function

  



def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))





def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)


def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')


def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
 

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')





def task1(request):
    books= Book.objects.filter(Q(price__lte = 80))
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task2(request):
    books= Book.objects.filter(Q(edition__gte = 3) & (Q(title__icontains='co') | Q(author__icontains='co')))
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task3(request):
    books= Book.objects.filter(~Q(edition__gte = 3) & (~Q(title__icontains='co') | ~Q(author__icontains='co')))
    return render(request, 'bookmodule/bookList.html', {'books':books})


def task4(request):
    books= Book.objects.order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task5(request):
    query = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        min_price=Min('price'),
        max_price=Max('price')
    )
    return render(request, 'bookmodule/task5.html', {'query':query})


def task7(request):
    cities= Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'cities':cities})


def task22(request):
    departments = Department11.objects.annotate(student_count=Count('students11'))
    return render(request, 'bookmodule/task22.html', {'departments':departments})


def task33(request):
    courses = Course11.objects.annotate(student_count=Count('students11'))
    return render(request, 'bookmodule/task33.html', {'courses':courses})


def task44(request):
    departments = Department11.objects.annotate(oldest_student_id=Min('students11__id'))
    
    department_data = []

    for department in departments:
        if department.oldest_student_id is not None:
            oldest_student = department.students11_set.get(id=department.oldest_student_id)
            department_data.append(
                {
                    'department_name': department.name,
                    'oldest_student_name': oldest_student.name
                }
            )

    return render(request, 'bookmodule/task44.html', {'department_data': department_data})


def task55(request):
    departments = Department11.objects.annotate(student_count=Count('students11')).filter(student_count__gt=2).order_by("-student_count")
    return render(request, 'bookmodule/task55.html', {'departments':departments})


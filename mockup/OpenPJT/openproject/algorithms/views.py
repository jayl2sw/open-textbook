from django.shortcuts import get_list_or_404, render
from .forms import AlgorithmForm
from .models import Algorithm

# Create your views here.
def index(request):
    algorithms = Algorithm.objects.all()
    context = {
        'algorithms': algorithms
    }
    return render(request,'algorithms/index.html', context)

def create(request):
    if request.method == "POST":
        pass
    else:
        form = AlgorithmForm
    context = {
        'form': form
    }
    return render(request, 'algorithms/create.html', context)
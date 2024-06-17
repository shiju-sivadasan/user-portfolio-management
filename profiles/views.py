from django.shortcuts import render,redirect
from .forms import PortfolioForm
from .models import Portfolio
# Create your views here.
def create_portfolio(request):
    frm=PortfolioForm()
    if request.POST:
        frm=PortfolioForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('portfolio_details')
    return render(request, 'userview/create_portfolio.html',{'frm':frm})

def portfolio_details(request):
    portfolio=Portfolio.objects.all()
    return render(request, 'userview/portfolio_details.html',{'portfolio':portfolio})

def update_portfolio(request,id):
    data=Portfolio.objects.get(id=id)
    portfolio=PortfolioForm(instance=data)
    if request.POST:
        portfolio=PortfolioForm(request.POST,request.FILES,instance=data)
        if portfolio.is_valid():
            portfolio.save()
            return redirect('portfolio_details')
    return render(request,'userview/portfolio_update.html',{'portfolio':portfolio})
from django.urls import path       
from . import views
urlpatterns = [
    path('create_portfolio/',views.create_portfolio,name="create_portfolio"),
    path('portfolio_details/',views.portfolio_details,name="portfolio_details"),
    path('portfolio_update/<int:id>',views.update_portfolio,name="portfolio_update"),
]
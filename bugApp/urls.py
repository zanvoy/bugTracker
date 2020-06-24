from django.urls import path
from bugApp import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('ticket/<int:id>/', views.ticketview, name='ticket'),  
    path('ticketadd/', views.ticketadd, name='ticketadd'),
    path('ticketedit/<int:id>/', views.ticket_edit, name='ticket_edit'),
    path('<username>', views.profile, name='profile'),
    path('assign/<int:id>', views.assign, name='assign'),
    path('unassign/<int:id>', views.unassign, name='unassign'),
    path('compleat/<int:id>', views.compleat, name='compleat'),
    path('invalid/<int:id>', views.invalid, name='invalid'),
]

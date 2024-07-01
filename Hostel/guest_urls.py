from django.urls import path

from Hostel.guest_views import ApplyLeave, IndexView, Book_hostel, hostels_detals, My_Room, View_room, leave_status, payment

urlpatterns = [

    path('',IndexView.as_view()),
    path('hostels_detals',hostels_detals.as_view()),
    path('Book',Book_hostel.as_view()),
    path('My_Room',My_Room.as_view()),
    path('View_room',View_room.as_view()),
    path('payment',payment.as_view()),
    path('ApplyLeave',ApplyLeave.as_view()),
    path('leave_status',leave_status.as_view())

]

def urls():
    return (urlpatterns,'guest','guest')
from django.urls import path

from Hostel.hostel_views import DisallowLeave, IndexView, Allocate_Room, LeaveViewList, SetAttedance, View_student, AddRoom, Rejectcart, allowLeave, attendence

urlpatterns = [
    path('',IndexView.as_view()),
    path('View_Booking',View_student.as_view()),
    path('add_Room',AddRoom.as_view()),
    path('Allocate_Room',Allocate_Room.as_view()),
    path('remove',Rejectcart.as_view()),
    path('attendence',attendence.as_view()),
    path('SetAttedance', SetAttedance.as_view()),
    path('LeaveViewList',LeaveViewList.as_view()),
    path('allowLeave',allowLeave.as_view()),
    path('DisallowLeave',DisallowLeave.as_view())


]

def urls():
    return (urlpatterns,'hostel','hostel')
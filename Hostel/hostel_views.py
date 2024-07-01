import datetime
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import  render
from django.views.generic import TemplateView, View
from .models import room 
from django.http import HttpResponse
from Hostel.models import Attendance, Hostel, LeaveApply, book, Room_alocate, room, student


class IndexView(TemplateView):
    template_name = 'hostel/index.html'

class View_student(TemplateView):
    template_name = 'hostel/view_booking.html'

    def get_context_data(self, **kwargs):

        context = super(View_student,self).get_context_data(**kwargs)

        view=student.objects.all()
        context['feed'] = view
        return context

class AddRoom(TemplateView):
    template_name = 'hostel/add_room.html'

    def post(self, request):
        room_type = request.POST['type']
        block = request.POST['block']
        room_number = request.POST['number']

        # Check if the room already exists
        existing_room = room.objects.filter( block=block, room_number=room_number).exists()
        if existing_room:
            return render(request, 'hostel/index.html', {'message': "Room already allocated"})
        else:
            new_room = room(room_type=room_type, room_number=room_number, block=block)
            new_room.save()
            return render(request, 'hostel/index.html', {'message': "Room successfully added"})
        
class Allocate_Room(TemplateView):
    template_name = 'hostel/allocate.html'

    def get_context_data(self, **kwargs):
        context = super(Allocate_Room, self).get_context_data(**kwargs)

        view = room.objects.all()
        context['feed'] = view
        return context

    def post(self,request):

        id = self.request.GET['id']

      
        name = request.POST['name']

        se=Room_alocate()
        se.guest_id=id
        se.roomId=name
        se.save()
        return render(request, 'hostel/index.html', {'message': "successfully added"})


class Rejectcart(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        book.objects.get(id=id).delete()
        return render(request, 'hostel/index.html', {'message': "Booking Removed"})


class attendence(TemplateView):
    template_name = 'hostel/attendence.html'

    def get_context_data(self, **kwargs):

        context = super(attendence,self).get_context_data(**kwargs)

        view=student.objects.all()
        context['feed'] = view
        return context

    
class SetAttedance(View):
    def dispatch(self, request, *args, **kwargs):

        stu = self.request.GET['stus']
        st = self.request.GET['st']


        s = student.objects.get(pk=stu)
     
        dat = datetime.date.today()
        co = Attendance.objects.filter(student=s, ab_date=dat).count()

        if(co > 0):
            return render(request, 'hostel/index.html', {'message': "Attendance already added to this student.."})

        else:
            if(st == 'Present'):

                a = Attendance()
                a.ab_date = datetime.date.today()
                a.ab_status = st
                a.student = s
                a.save()

                return render(request, 'hostel/index.html', {'message': "Attendance Added.."})
            else:
                dat = datetime.date.today()
                print(dat)
                a = Attendance()
                a.ab_date = dat
                a.ab_status = st
                a.student = s
                a.save()
                
                return render(request, 'hostel/index.html', {'message': "Attendance Added.."})
class LeaveViewList(TemplateView):
    template_name = 'hostel/leaverequest.html'

    def get_context_data(self, **kwargs):
        context = super(LeaveViewList, self).get_context_data(**kwargs)
        m = LeaveApply.objects.all()

        context['m'] = m
        return context
    

class allowLeave(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = LeaveApply.objects.get(pk=id)
        user.status = 'Approve'
        user.save()

        return render(request, 'hostel/index.html', {'message': "Leave Approved"}) 

class DisallowLeave(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = LeaveApply.objects.get(pk=id)
        user.status = 'Reject'
        user.save()

        return render(request, 'hostel/index.html', {'message': "Leave Rejected"})
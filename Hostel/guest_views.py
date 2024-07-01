from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User

from Hostel.models import Hostel, LeaveApply, book, student, Room_alocate, room


class IndexView(TemplateView):
    template_name = 'guest/index.html'

class hostels_detals(TemplateView):
    template_name = 'guest/team.html'
    def get_context_data(self, **kwargs):
        context = super(hostels_detals, self).get_context_data(**kwargs)
        view_pp = Hostel.objects.all()
        context['view_pp'] = view_pp
        return context

class Book_hostel(TemplateView):
    template_name = 'guest/book.html'

    def post(self,request):

        id = self.request.GET['id']
        id2 = self.request.GET['id2']
        price=room.objects.get(id=id)

        pr=price.price

        gu = student.objects.get(user_id=self.request.user.id)

        check = request.POST['check']
        no = request.POST['no']
        total=int(pr)*int(no)
        if book.objects.filter(room_id=id2):
            return render(request, 'guest/index.html', {'message': "Room Already Booked"})
        else:
            se = book()
            se.hostel_id = id2
            se.room_id = id
            se.Check_in = check
            se.Duration = no
            se.Total = total
            se.guest_id = gu.id
            se.status = 'selected'
            se.payment = 'null'

            se.save()
            return render(request, 'guest/payment.html', {'price': total})

class My_Room(TemplateView):
    template_name = 'guest/view_room.html'

    def get_context_data(self, **kwargs):
        context = super(My_Room, self).get_context_data(**kwargs)

        view_book = student.objects.get(user_id=self.request.user.id)
        view = book.objects.filter(guest_id=view_book.id)
        context['feed'] = view
        return context

class View_room(TemplateView):
    template_name = 'guest/view_hostel_room.html'
    def get_context_data(self, **kwargs):
        context = super(View_room, self).get_context_data(**kwargs)
        view_pp = room.objects.all()
        context['view_pp'] = view_pp
        return context
    

    
class payment(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        gu = student.objects.get(user_id=self.request.user.id)

        ch = book.objects.filter(guest_id=gu.id,payment='null')
        print(ch)
        for i in ch:
            i.payment = 'paid'
            i.save()
        return render(request, 'guest/index.html', {'message': " payment Success"})
    
class ApplyLeave(TemplateView):
    template_name = 'guest/leave.html'


    def post(self, request, *args, **kwargs):
        s = student.objects.get(user__id=self.request.user.id)
     
        a = LeaveApply()
        
        a.leave_from = request.POST['from']
        a.leave_till = request.POST['till']

        a.reason = request.POST['reason']
        a.student = s
        a.status = 'Apply'
        a.save()
        return render(request, 'guest/index.html', {'message': "Application sent.."})
    
    
class leave_status(TemplateView):
    template_name = 'guest/leave_status.html'
    def get_context_data(self, **kwargs):
        context = super(leave_status, self).get_context_data(**kwargs)
        gu = student.objects.get(user_id=self.request.user.id)

        view_pp = LeaveApply.objects.filter(student_id=gu.id)
        context['view_pp'] = view_pp
        return context
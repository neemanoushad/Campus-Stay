from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.checks import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from Hostel.models import student, UserType, Hostel,student


class IndexView(TemplateView):
    template_name = 'index.html'



class Guest_reg(TemplateView):
    template_name = 'user_register.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        contact = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gender']

        parent_contact = request.POST['parent_contact']
        parent_name = request.POST['parent_name']
        password = request.POST['password']
        try:
            user = User.objects._create_user(username=email,password=password,first_name=fullname,email=email,last_name =1)
            user.save()
            stu = student()
            stu.user=user
            stu.contact = contact
            stu.parent_contact = parent_contact
            stu.parent_name = parent_name
            stu.address = address
            stu.gender = gender
            stu.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "student"
            usertype.save()
            return render(request,'user_register.html',{'message':"successfully added"})
        except:
            return render(request,'user_register.html',{'message':"successfully added"})

class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/hostel')
                elif UserType.objects.get(user_id=user.id).type == "student":
                    return redirect('/student')
                

            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})



class Hostel_reg(TemplateView):
    template_name = 'hostel_register.html'

    def post(self, request, *args, **kwargs):
        fullname = request.POST['name']
        contact = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        image = request.FILES['image']

        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
        owner = request.POST['owner']

        categoy = request.POST['categoy']
        rent = request.POST['rent']

        password = request.POST['password']
        try:
            user = User.objects._create_user(username=email, password=password, first_name=fullname, email=email,
                                             last_name=0)
            user.save()
            student = Hostel()
            student.user = user
            student.contact = contact
            student.hostel_category = categoy
            student.address = address
            student.rent=rent
            student.owner = owner
            student.image = filesss
            student.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "hostel"
            usertype.save()
            return render(request, 'user_register.html', {'message': "successfully added"})
        except:
            return render(request, 'user_register.html', {'message': "successfully added"})
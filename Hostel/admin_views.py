# import datetime
# from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect, render
# from django.views.generic import TemplateView, View

# from Hostel.models import Guest, Hostel


# class IndexView(TemplateView):
#     template_name = 'hostel/index.html'



# class HostelsView(TemplateView):
#     template_name = 'admin/hostels.html'

#     def get_context_data(self, **kwargs):
#         context = super(HostelsView,self).get_context_data(**kwargs)
#         # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

#         # guest = User.objects.filter(last_name='0',is_staff='1')
#         user = User()
#         hostel = Hostel.objects.filter(user__last_name='1',user__is_active='1')
#         # context['users'] = guest
#         context['hostel'] =  hostel
#         return context


# class UsersView(TemplateView):
#     template_name = 'admin/users.html'

#     def get_context_data(self, **kwargs):
#         context = super(UsersView,self).get_context_data(**kwargs)
#         # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

#         # guest = User.objects.filter(last_name='0',is_staff='1')
#         user = User()
#         student = Guest.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
#         # context['users'] = guest
#         context['student'] =  student
#         return context



# class NewUsersView(TemplateView):
#     template_name = 'admin/new_users.html'

#     def get_context_data(self, **kwargs):
#         context = super(NewUsersView,self).get_context_data(**kwargs)

#         student = Guest.objects.filter(user__last_name='0',user__is_staff='0', user__is_active='1')
#         context['new'] =  student
#         return context



# class NewHostelsView(TemplateView):
#     template_name = 'admin/new_hostels.html'

#     def get_context_data(self, **kwargs):
#         context = super(NewHostelsView, self).get_context_data(**kwargs)

#         user = Hostel.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')

#         context['user'] = user
#         return context




# class ApproveView(View):
#     def dispatch(self, request, *args, **kwargs):

#         id = request.GET['id']
#         user = User.objects.get(pk=id)
#         user.last_name='1'
#         user.save()
#         return render(request,'admin/index.html',{'message':" Account Approved"})



# class RejectView(View):
#     def dispatch(self, request, *args, **kwargs):
#         id = request.GET['id']
#         user = User.objects.get(pk=id)
#         user.last_name='1'
#         user.is_active='0'
#         user.save()
#         return render(request,'admin/index.html',{'message':"Account Removed"})




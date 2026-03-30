from django.shortcuts import render, redirect, HttpResponse 
from django.http import JsonResponse
from django.contrib import messages
from website_app.models import Property
from website_app.models import Category_registration
from website_app.models import Contact_data
# from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from django.http import FileResponse, Http404


# Create your views here.
def home(request):
      return render (request,'main.html')

@login_required(login_url='Login')
def PropertyAdd(request):
      if request.method == "POST":
            name = request.POST['name']
            agency = request.POST['agency']
            phone = request.POST['phone']
            upload_file = request.FILES['uploadfile']
            upload_img = request.FILES['upload_image']
            address = request.POST['address']
            property = Property.objects.create(name=name, agency=agency, phone=phone, uploadfile= upload_file, upload_img= upload_img,addre=address)
            property.save()
            print(request.POST)
            # try:
            #   return FileResponse(open('foobar.pdf', 'rb'), content_type='application/pdf')
            # except FileNotFoundError:
            #  raise Http404()
            messages.success(request, "Your form submited successfully.")
            return render(request, 'Property.html')
      else:
            # return JsonResponse({'status': 'ok'})
            return render(request, 'Property.html')

@login_required(login_url='Login')
def Architect(request):
    viewarchitect_data = Category_registration.objects.filter(desic='architecture')
    data = {'form': viewarchitect_data}
    return render(request, 'Architect.html', data)

@login_required(login_url='Login')
def Solar_Firms (request):
      viewsolar_data = Category_registration.objects.filter(desic='solar')
      data={'form':viewsolar_data}
      return render (request, 'Solar_Firms.html',data)

@login_required(login_url='Login')
def Soil_Firms (request):
      viewsoil_data = Category_registration.objects.filter(desic='soil')
      data={'form':viewsoil_data}
      return render (request, 'Soil_Firms.html',data)

@login_required(login_url='Login')
def Vetting_Engineers (request):
      viewvetting_data = Category_registration.objects.filter(desic='Vetting')
      data={'form':viewvetting_data}
      return render (request, 'Vetting_Engineers.html',data)

def Registerform (request):
      return render (request, 'Register.html')

def Contactform (request):
      if request.method == "POST":
           name = request.POST['name']
           email = request.POST['email']
           cnic = request.POST ['cnic']
           phone = request.POST['phone']
           comment = request.POST['comment']
           Contact =Contact_data.objects.create(name=name, email=email, cnic=cnic, phone=phone, comment=comment)
           messages.success(request, "Your feedback submitted successfully.")
           return render(request, 'Contact.html')
      else:
	        return render(request, 'Contact.html')

# def Category_registrationform (request):
      #   if request.method == "POST":
      #       reg_no = request.POST['reg_no']
      #       name = request.POST['name']
      #       firm = request.POST['firm']
      #       phone = request.POST['phone']
      #       desic = request.POST['desic']
      #       address = request.POST['address']
      #       categ = Category_registration.objects.create(reg_no=reg_no,name=name, firm=firm, phone=phone, desic=desic,addre=address)
      #       categ.save()
      #       messages.success(request, "Your form submited successfully.")
      #       return render (request, 'Category_registration.html')
      #   else:
      #         return render (request, 'Category_registration.html')
      
def Category_registrationform(request):
      if request.method == "POST":
            reg_no = request.POST['reg_no']
            name = request.POST['name']
            firm = request.POST['firm']
            phone = request.POST['phone']
            upload_file = request.FILES['up_file']
            upload_img = request.FILES['up_image']
            desic = request.POST['desic']
            address = request.POST['address']
        
            categ = Category_registration.objects.create(
                  reg_no=reg_no,
                  name=name,
                  firm=firm,
                  phone=phone,
                  uploadfile= upload_file, 
                  upload_img= upload_img,
                  desic=desic,
                  addre=address
            )
            categ.save()
        
            messages.success(request, "Thank you for connecting with The Grand Palace. We will connect with you soon.")
            viewcateg_data = Category_registration.objects.all()
            data = {'form': viewcateg_data}
            return render(request, 'Category_registration.html', data)
      else:
            designations = Category_registration.objects.values('desic').distinct()
            data = {'data_desic': designations}
            return render(request, 'Category_registration.html', data)

      
@login_required(login_url='Login')      
def View_property (request):
      viewproperty_data = Property.objects.all()
      data={'form':viewproperty_data}
      return render (request, 'View_property.html',data)


def Updateform(request,reg_no):      
      data =Category_registration.objects.get(reg_no=reg_no)
      print('data',data)  
      if request.method == 'POST':
            name = request.POST['name']
            firm = request.POST['firm']
            phone = request.POST['phone']
            # desic = request.POST['desig_choice']
            uploadfile = request.FILES['up_file']
            upload_img = request.FILES['up_image']
            addre = request.POST['address']
            data.name = name
            data.firm = firm
            data.phone = phone
            data.uploadfile= uploadfile 
            data.upload_img= upload_img
            data.addre = addre 
            data.save()
            messages.success(request, "Record updated successfully.")
            return redirect('Architect')
      # return redirect('Update_form.html')
      return render (request, 'Update_form.html',{'data':data})


def DeleteRecord(request,reg_no):
      record=Category_registration.objects.get(reg_no=reg_no)
      record.delete()
      messages.success(request, "Record deleted successfully.")
      return redirect('Architect')

# property update and delete record

def Update_property(request,agency):
       
      data =Property.objects.get(agency = agency)
      print('data',data)  
      if request.method == 'POST':
            name = request.POST['name']
            firm = request.POST['firm']
            phone = request.POST['phone']
            addre = request.POST['address']
            print(addre)
            data.name = name
            data.firm = firm
            data.phone = phone
            data.addre = addre
            data.save()
            messages.success(request, "Record updated successfully.")
            return redirect('View_property')
      # return redirect('Update_form.html')
      return render (request, 'Update_form.html',{'data':data})


def Delete_property(request,agency):
      record=Property.objects.get(agency=agency)
      record.delete()
      messages.success(request, "Record deleted successfully.")
      return redirect('View_property')

#Login page
def Login_page(request):
      print('login function')
      if request.method == "POST":
            username= request.POST['username']
            psw1= request.POST['psw']
            user=authenticate(request,username=username,password=psw1)
            if user is not None:
                   login(request,user)
                   return redirect('home')
                   messages.success(request, "Your login successfully.")
            else:
              return messages.error(request, "Incorrect login information")
      return render(request, 'Login.html')
      return redirect('Register')

#Signun Page
def Signup_page(request):
      if request.method == "POST":
            email = request.POST['email']
            username = request.POST['username']
            pass1 = request.POST['psw1']
            pass2 = request.POST['con_psw']

            user = User.objects.filter(username=username)
            if user.exists():
                   messages.info(request, "username alreday taken.")
                   return redirect('Signup')
            
            if pass1!=pass2:
               messages.success(request, "Your password and confirm password are not same!")
               
            else:
              my_user = User.objects.create_user(username,email,pass1)
              my_user.save()
              messages.success(request, "user created thier account successfully.")

            return redirect('Login')
      return render(request,'Signup.html')
      
def Logout_page(request):
      logout(request)
      return redirect('Login')

from django.contrib.auth import authenticate, update_session_auth_hash
from django.shortcuts import render, redirect
from .models import EventGallary, AlumniInfo
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth, User
from django.contrib import messages


def home(request):
    return render(request,'HomePage.html')

def about(request):
    return render(request,'about_us.html')

def contact(request):
    return render(request,'contact_us.html')

def register(request):
    if request.method== 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        address= request.POST.get('address')
        about_alumni= request.POST.get('about_alumni')
        mob1= request.POST.get('mob1')
        mob2= request.POST.get('mob2')
        email= request.POST.get('email')
        passout= request.POST.get('passout')
        branch= request.POST.get('branch')
        prn_no= request.POST.get('prn_no')
        job_status= request.POST.get('job_status')
        org_name= request.POST.get('org_name')
        username= request.POST.get('username')
        pass1= request.POST.get('pass1')
        pass2= request.POST.get('pass2')
        # print(first_name,last_name,address,about_alumni,mob2,mob1,email,passout,branch,prn_no,job_status,org_name,username,pass1,pass2)
        # message
        if pass1==pass2 and email==username:
            if User.objects.filter(username=username):
                msgs = "Yes"
                msg='Username is Already Exist'

                return render(request,'registration.html',locals())
            else:
                user_reg= User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=pass1,is_superuser='False')
                user_reg.save()

                alumni_info=AlumniInfo(first_name=first_name,last_name=last_name,address=address,about_alumni=about_alumni,mob1=mob1,mob2=mob2,email=email,passout=passout,branch=branch,prn_no=prn_no,job_status=job_status,org_name=org_name)
                alumni_info.save()
                msgs = "Yes"
                msg="Registration Successful Now You Can Login"
                return render(request,'user_login_Page.html',locals())
        else:
            msgs = "Yes"
            msg='Password Does not match or Username is not Email'
            return render(request,'registration.html',locals())
    else:

        return render(request,'registration.html')


def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        a = User.objects.get(username=username)
        spr = a.is_superuser

        if spr == True:
            user = auth.authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                auth.login(request, user)
                msgs = "Yes"
                msg= "Logged in Successfully"
                return render(request, 'admin_log.html',locals())
            else:
                msgs = "Yes"
                msg = "Enter Valid Credentials"
                return render(request, 'admin_login_Page.html',locals())
        else:
            msgs = "Yes"
            msg = "You are not admin please Login from user Login"
            return render(request, 'admin_login_Page.html', locals())


    else:
        return render(request, 'admin_login_Page.html')


def userlogin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        a= User.objects.get(username=username)
        spr=a.is_superuser

        if spr==False:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                msgs="Yes"
                msg="Logged in Successfully"
                return render(request, 'user_log.html',locals())
            else:
                msgs = "Yes"
                msg = "Enter Valid Credentials"
                return render(request, 'user_login_Page.html',locals())
        else:
            msgs = "Yes"
            msg = "You are an admin please Login from admin Login"
            return render(request, 'user_login_Page.html',locals())


    else:
        return render(request, 'user_login_Page.html')




def addalumni(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        about_alumni = request.POST.get('about_alumni')
        mob1 = request.POST.get('mob1')
        mob2 = request.POST.get('mob2')
        email = request.POST.get('email')
        passout = request.POST.get('passout')
        branch = request.POST.get('branch')
        prn_no = request.POST.get('prn_no')
        job_status = request.POST.get('job_status')
        org_name = request.POST.get('org_name')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        addanother=request.POST.get('addanother','off')

        if pass1==pass2 and email==username:
            if User.objects.filter(username=username):
                msgs = "Yes"
                msg='Username is Already Exist'

                return render(request,'add_alumni.html',locals())
            else:
                user_reg= User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=pass1,is_superuser='False')
                alumni_info=AlumniInfo(first_name=first_name,last_name=last_name,address=address,about_alumni=about_alumni,mob1=mob1,mob2=mob2,email=email,passout=passout,branch=branch,prn_no=prn_no,job_status=job_status,org_name=org_name)

                if addanother=="on":
                    user_reg.save()
                    alumni_info.save()
                    msgs="Yes"
                    msg = "Registration Successful"
                    return render(request, 'add_alumni.html',locals())
                else:
                    user_reg.save()
                    alumni_info.save()
                    msgs="Yes"
                    msg="Alumnus Added Successfully"
                    return render(request, 'admin_log.html',locals())


        else:
            msg='Password Does not match or Username is not provided Email'
            return render(request,'add_alumni.html',locals())
    else:

        return render(request,'add_alumni.html')





def viewalumni(request):
    alumnis = AlumniInfo.objects.all()
    if request.method=="POST":
        search=request.POST.get('search')
        if search!=None:
            alumnis1=[]
            for alumni in alumnis:
                if search.lower() in alumni.first_name.lower() or search.lower() in alumni.last_name.lower():
                    # alumnis1=AlumniInfo.objects.filter(first_name=search)
                    alumnis1.append(alumni)
            return render(request, 'view_alumni.html', {'alumnis': alumnis1})

        else:
            msgs = "Yes"
            msg="Enter Something In Search Box"

            return render(request, 'view_alumni.html', {'alumnis': alumnis,"msgs":msgs,"msg":msg})


    else:

        return render(request,'view_alumni.html',{'alumnis':alumnis})



def gallary(request):
    events=EventGallary.objects.all()
    pastevenets=[]
    upevenets=[]
    tdate = datetime.datetime.now().date()

    for event in events:
        edate1 = EventGallary.objects.get(event_name=event.event_name)
        edate2=edate1.event_date

        if tdate <= edate2:
            upevenets.append(event)
        else:
            pastevenets.append(event)




    return render(request,'gallary.html',{'pastevenets': pastevenets,'upevenets':upevenets})

def addgallary(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_date = request.POST.get('event_date')
        event_img = request.FILES.get('event_img')
        event_desc = request.POST.get('event_desc')
        myevent = EventGallary(event_name=event_name, event_date=event_date, event_img=event_img, event_desc=event_desc)
        myevent.save()
        msgs="Yes"
        msg="Event Successfully Added to Gallary "
        return render(request, 'admin_log.html',locals())
    else:
        return render(request,'AddGallary.html')


def logout(request):
    auth.logout(request)
    msgs = "Yes"
    msg="Logout Successfully"
    return render(request,'HomePage.html',locals())

def userhome(request):

    return render(request,'user_log.html')


def adminhome(request):
    return render(request,'admin_log.html')

def admin_updateprofile(request, id):

    if request.method=="POST":
        c_user=AlumniInfo.objects.get(id=id)
        user1 = User.objects.get(email=c_user.email)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        about_alumni = request.POST.get('about_alumni')
        mob1 = request.POST.get('mob1')
        mob2 = request.POST.get('mob2')

        passout = request.POST.get('passout')
        branch = request.POST.get('branch')
        prn_no = request.POST.get('prn_no')
        job_status = request.POST.get('job_status')
        org_name = request.POST.get('org_name')

        c_user.first_name=first_name
        c_user.last_name=last_name
        c_user.address=address
        c_user.about_alumni=about_alumni
        c_user.mob1=mob1
        c_user.mob2=mob2
        c_user.passout=passout
        c_user.branch=branch
        c_user.prn_no=prn_no
        c_user.job_status=job_status
        c_user.org_name=org_name
        c_user.save()

        user1.first_name = first_name
        user1.last_name = last_name
        user1.save()
        msgs = "Yes"
        msg="Details Updated Successfully"
        return render(request,"admin_log.html",locals())

    c_user = AlumniInfo.objects.get(id=id)
    return render(request,'admin_updateprofile.html',{'c_user':c_user})

def admin_deletealumni(request,id):
    c_user = AlumniInfo.objects.get(id=id)
    user1 = User.objects.get(email=c_user.email)
    # user = User.objects.get(id=id)
    # print(user)
    user1.delete()
    c_user.delete()

    alumnis = AlumniInfo.objects.all()
    msgs="Yes"
    msg="Alumnus Deleted Successfully"
    return render(request, 'view_alumni.html', locals())


def branch_Alumni(request):
    curr_user = request.user
    c_user = AlumniInfo.objects.get(email=curr_user)
    branch=c_user.branch

    branch_alumnis= AlumniInfo.objects.filter(branch=branch)

    if request.method=="POST":
        search=request.POST.get('search')
        # branch_alumnis = AlumniInfo.objects.filter(branch=branch)
        print(search)
        print(branch_alumnis)
        if search!=None:
            branch_alumnis1=[]
            for alumni in branch_alumnis:
                if search.lower() in alumni.first_name.lower() or search.lower() in alumni.last_name.lower():
                    # alumnis1=AlumniInfo.objects.filter(first_name=search)
                    branch_alumnis1.append(alumni)
            if len(branch_alumnis1)==0:
                msgs = "Yes"
                msg = "No match found to your search"
                return render(request, 'branch_Alumni.html', {'alumnis': branch_alumnis,"msgs":msgs,"msg":msg})
            else:
                return render(request, 'branch_Alumni.html', {'alumnis': branch_alumnis1})
        else:
            msgs="Yes"
            msg="Enter Some text in Search Box"
            return render(request, 'branch_Alumni.html', {'alumnis': branch_alumnis,"msgs":msgs,"msg":msg})
    return render(request, 'branch_Alumni.html', {'alumnis': branch_alumnis})

def updateyourprofile(request):
    curr_user = request.user

    c_user = AlumniInfo.objects.get(email=curr_user)
    if request.method=="POST":
        user1=User.objects.get(email=curr_user)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        about_alumni = request.POST.get('about_alumni')
        mob1 = request.POST.get('mob1')
        mob2 = request.POST.get('mob2')

        passout = request.POST.get('passout')
        branch = request.POST.get('branch')
        prn_no = request.POST.get('prn_no')
        job_status = request.POST.get('job_status')
        org_name = request.POST.get('org_name')

        c_user.first_name=first_name
        c_user.last_name=last_name
        user1.first_name=first_name
        user1.last_name=last_name
        c_user.address=address
        c_user.about_alumni=about_alumni
        c_user.mob1=mob1
        c_user.mob2=mob2
        c_user.passout=passout
        c_user.branch=branch
        c_user.prn_no=prn_no
        c_user.job_status=job_status
        c_user.org_name=org_name
        c_user.save()
        user1.save()
        msgs="Yes"
        msg="Profile Updated Successfully"
        return render(request,"user_log.html",locals())


    return render(request,'userprofileupdate.html',{'c_user':c_user})

def changeuserpassword(request):
    if request.method== "POST":
        # req= request.user
        oldpass=request.POST.get('oldpass')
        pass1=request.POST.get('newpass1')
        pass2=request.POST.get('newpass2')
        username=request.POST.get('username')
        user = authenticate(username=username, password=oldpass)

        if user is not None:
            req=User.objects.get(username=username)
            if pass1==pass2:
                req.set_password(pass1)
                req.save()
                update_session_auth_hash(request, req)
                auth.logout(request)
                msgs="Yes"
                msg="Password Changed Successfully, Log in again with new password"
                return render(request, 'HomePage.html',locals())

            else:
                msgs="Yes"
                msg="Please Check your new Password"
                return render (request,'admin_change_password.html',locals())

        else:
            msgs="Yes"
            msg="Wrong Old Password"
            return render(request, 'admin_change_password.html',locals())
    return render(request,'user_change_password.html')
import smtplib
from email.mime.text import MIMEText

from django.shortcuts import render,HttpResponse
from myapp.models import *
import random
import datetime
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
# Create your views here.
def admin_home(request):
    return render(request,'admin/adminindex.html')
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def login_post(request):
    name=request.POST['uname']
    paswrd=request.POST['pass']
    log=Login.objects.filter(username=name,password=paswrd)
    if log.exists():
        logid=log[0].id
        request.session['lid']=logid
        if log[0].usertype == 'admin':
            return HttpResponse("<script>alert('login sucess');window.location='admin_home'</script>")
        elif log[0].usertype == 'expert':
            return HttpResponse("<script>alert('login sucess');window.location='expert_home'</script>")
        elif log[0].usertype == 'staff':
            return HttpResponse("<script>alert('login sucess');window.location='staff_home'</script>")
        elif log[0].usertype == 'parent':
            return HttpResponse("<script>alert('login sucess');window.location='parent_home'</script>")
        else:
            return HttpResponse("<script>alert('invalid user');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('plaese check your data');window.location='/'</script>")

def logout(request):
    request.session['lid'] =''
    return HttpResponse("<script>alert('logout success');window.location='/'</script>")


def add_expert(request):
    if  request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request,'admin/add_expert.html')

def add_expert_post(request):
    name=request.POST['textfield']
    quli=request.POST['textfield2']
    spec=request.POST['textfield3']
    exp=request.POST['textfield4']
    email=request.POST['textfield5']
    phn=request.POST['textfield6']
    log=Login.objects.filter(username=email)
    rd=random.randint(0000,9999)
    if log.exists():
        return HttpResponse("<script>alert('this user already exists');window.location='/admin_home'</script>")
    else:
        lo=Login()
        lo.username=email
        lo.password=rd
        lo.usertype='expert'
        lo.save()

        obj=Expert()
        obj.name=name
        obj.specialization=spec
        obj.qualification=quli
        obj.experience=exp
        obj.email=email
        obj.phone=phn
        obj.LOGIN=lo
    #     gmail = smtplib.SMTP('smtp.gmail.com', 587)
    #
    #     gmail.ehlo()
    #
    #     gmail.starttls()
    #
    #     gmail.login('riss.athulchandran@gmail.com', 'cjcyiddroayvvpqn')
    #
    #     print("Couldn't setup email!!" + str(e))
    #
    #     msg = MIMEText("Your Password is " + str(rd))
    #
    #     msg['Subject'] = 'Verification'
    #
    #     msg['To'] = email
    #
    #     msg['From'] = 'riss.athulchandran@gmail.com'
    #
    # try:
    #
    #     gmail.send_message(msg)
    #
    # except Exception as e:
    #
    #     print("COULDN'T SEND EMAIL", str(e))

        obj.save()

        return HttpResponse("<script>alert('added');window.location='admin_home'</script>")

def view_expert(request):
    if  request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Expert.objects.all()
        return render(request,'admin/view_expert.html',{'data':data})

def edit_expert(request,id):
    if  request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Expert.objects.get(id=id)
        return render(request,'admin/edit_expert.html',{'data':data})

def edit_expert_post(request,id):
    nam = request.POST['textfield']
    quli = request.POST['textfield2']
    spec = request.POST['textfield3']
    exp = request.POST['textfield4']
    email = request.POST['textfield5']
    phn = request.POST['textfield6']
    Expert.objects.filter(id=id).update(name=nam,qualification=quli,specialization=spec,experience=exp,email=email,phone=phn)
    return HttpResponse("<script>alert('edited');window.location='/view_expert'</script>")

def delete_expert(request,id):
    Login.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_expert'</script>")

def add_staff(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request,'admin/add_staff.html')

def add_staff_post(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    quli=request.POST['textfield5']
    exp=request.POST['textfield6']
    emil=request.POST['textfield7']
    gen=request.POST['RadioGroup1']
    phn=request.POST['textfield8']
    log=Login.objects.filter(username=emil)
    rd = random.randint(0000, 9999)
    if log.exists():
        return HttpResponse("<script>alert('this user already exists');window.location='/admin_home'</script>")
    else:
        logi=Login()
        logi.username=emil
        logi.password=rd
        logi.usertype='staff'
        logi.save()

        obj=Staff()
        obj.name=name
        obj.place=place
        obj.post=post
        obj.pin=pin
        obj.qualification=quli
        obj.experience=exp
        obj.email=emil
        obj.gender=gen
        obj.phone=phn
        obj.LOGIN=logi
    #     gmail = smtplib.SMTP('smtp.gmail.com', 587)
    #
    #     gmail.ehlo()
    #
    #     gmail.starttls()
    #
    #     gmail.login('riss.athulchandran@gmail.com', 'cjcyiddroayvvpqn')
    #
    #     print("Couldn't setup email!!" + str(e))
    #
    #     msg = MIMEText("Your Password is " + str(rd))
    #
    #     msg['Subject'] = 'Verification'
    #
    #     msg['To'] = email
    #
    #     msg['From'] = 'riss.athulchandran@gmail.com'
    #
    # try:
    #
    #     gmail.send_message(msg)
    #
    # except Exception as e:
    #
    #     print("COULDN'T SEND EMAIL", str(e))
        obj.save()
        return HttpResponse("<script>alert('staff aaded');window.location='/admin_home'</script>")


def view_staff(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Staff.objects.all()
        return render(request,'admin/view_staff.html',{'data':data})

def edit_staff(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Staff.objects.get(id=id)
        return render(request,'admin/edit_staff.html',{'data':data})

def edit_staff_post(request,id):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    quli = request.POST['textfield5']
    exp = request.POST['textfield6']
    emil = request.POST['textfield7']
    gen = request.POST['RadioGroup1']
    phn = request.POST['textfield8']
    Staff.objects.filter(id=id).update(name=name,place=place,post=post,pin=pin,qualification=quli,experience=exp,email=emil,gender=gen,phone=phn)
    return HttpResponse("<script>alert('staff edited');window.location='/view_staff'</script>")

def delete_staff(request,id):
    Login.objects.get(id=id).delete()
    return HttpResponse("<script>alert('staff edited');window.location='/view_staff'</script>")

def add_bus(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request,'admin/add_bus.html')


def add_bus_post(request):
    busno=request.POST['textfield']
    data=bus()
    data.vehicleno=busno
    data.save()
    return HttpResponse("<script>alert('added');window.location='/admin_home'</script>")

def view_bus(request):
    data=bus.objects.all()
    return render(request,'admin/view_bus.html',{'data':data})

def delete_bus(request,id):
    bus.objects.get(id=id).delete()
    return  HttpResponse("<script>alert('added');window.location='/view_bus'</script>")


def add_driver(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request, 'admin/add_driver.html')

def add_driver_post(request):
    name=request.POST['textfield']
    emil=request.POST['textfield2']
    phn=request.POST['textfield3']
    licsnc=request.POST['textfield4']
    lati=request.POST['textfield5']
    longi=request.POST['textfield6']
    exp=request.POST['textfield7']
    log = Login.objects.filter(username=emil)
    rd = random.randint(0000, 9999)
    if log.exists():
        return HttpResponse("<script>alert('this user already exists');window.location='/admin_home'</script>")
    else:
        logi = Login()
        logi.username = emil
        logi.password = rd
        logi.usertype = 'driver'
        logi.save()

        obj=Driver()
        obj.name=name
        obj.email=emil
        obj.phone=phn
        obj.licenseno=licsnc
        obj.experience=exp
        obj.LOGIN=logi
        obj.lattitude=lati
        obj.longitude=longi
    #     gmail = smtplib.SMTP('smtp.gmail.com', 587)
    #
    #     gmail.ehlo()
    #
    #     gmail.starttls()
    #
    #     gmail.login('riss.athulchandran@gmail.com', 'cjcyiddroayvvpqn')
    #
    #     print("Couldn't setup email!!" + str(e))
    #
    #     msg = MIMEText("Your Password is " + str(rd))
    #
    #     msg['Subject'] = 'Verification'
    #
    #     msg['To'] = email
    #
    #     msg['From'] = 'riss.athulchandran@gmail.com'
    #
    # try:
    #
    #     gmail.send_message(msg)
    #
    # except Exception as e:
    #
    #     print("COULDN'T SEND EMAIL", str(e))
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/admin_home'</script>")

def view_driver(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Driver.objects.all()
        return render(request, 'admin/view_driver.html',{'data':data})

def edit_driver(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data = Driver.objects.get(id=id)
        return render(request, 'admin/edit_driver.html', {'data': data})

def edit_driver_post(request,id):
    name = request.POST['textfield']
    emil = request.POST['textfield2']
    phn = request.POST['textfield3']
    licsnc = request.POST['textfield4']
    exp = request.POST['textfield5']
    lati = request.POST['textfield6']
    longi = request.POST['textfield7']
    Driver.objects.filter(id=id).update(name=name,email=emil,phone=phn,licenseno=licsnc,experience=exp,lattitude=lati,longitude=longi)
    return HttpResponse("<script>alert('edited');window.location='/view_driver'</script>")

def delete_driver(request,id):
    Driver.objects.get(id=id).delete()
    return HttpResponse("<script>alert('edited');window.location='/view_driver'</script>")

def assign_bus_todriver(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Driver.objects.all()
        data1=bus.objects.all()
        return render(request,'admin/allocate_bus_todriver.html',{'data':data,'data1':data1})

def assign_bus_todriver_post(request):
    dr=request.POST['select']
    bs=request.POST['select2']
    dat=Busassign_driver()
    dat.DRIVER_id=dr
    dat.BUS_id=bs
    dat.save()
    return HttpResponse("<script>alert('assigned');window.location='/admin_home'</script>")

def view_student(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Student.objects.all()
        return render(request,'admin/view_student.html',{'data':data})

def allocate_bus(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=bus.objects.all()
        return render(request,'admin/allocate_bus_tostudent.html',{'sid':id,'data':data})

def allocate_bus_post(request,id):
    bs=request.POST['select']
    obj=Busassign_student()
    obj.STUDENT=Student.objects.get(id=id)
    obj.BUS_id=bs
    obj.save()
    return HttpResponse("<script>alert('assigned');window.location='/admin_home'</script>")
def view_parents(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=parent.objects.all()
        return render(request,'admin/verify_parent.html',{'data':data})


def approve_parent(request,id):
    Login.objects.filter(id=id).update(usertype='parent')
    return HttpResponse("<script>alert('assigned');window.location='/admin_home'</script>")


def reject_parent(request, id):
    Login.objects.filter(id=id).update(usertype='reject')
    return HttpResponse("<script>alert('assigned');window.location='/admin_home'</script>")


# ===================================Expert==================================================================================

def expert_home(request):
    return render(request,'Expert/expertindex.html')
def view_profile(request):
   data=Expert.objects.get(LOGIN=request.session['lid'])
   return render(request,'Expert/view_profile.html',{'data':data})

def add_tips(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request,'Expert/add_tips.html')

def add_tips_post(request):
    tip=request.POST['textarea']
    date=datetime.datetime.now().strftime('%Y-%m-%d')
    data=Tips()
    data.tips=tip
    data.date=date
    data.EXPERT=Expert.objects.get(LOGIN=request.session['lid'])
    data.save()
    return HttpResponse("<script>alert('added');window.location='/expert_home'</script>")

def view_tips(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Tips.objects.filter(EXPERT__LOGIN=request.session['lid'])
        return render(request, 'Expert/view_tips.html',{'data':data})

def edit_tips(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data = Tips.objects.get(id=id)
        return render(request, 'Expert/edit_tips.html', {'data': data})

def edit_tips_post(request,id):
    tip = request.POST['textarea']
    Tips.objects.filter(id=id).update(tips=tip)
    return HttpResponse("<script>alert('edited');window.location='/view_tips'</script>")

def delete_tips(request,id):
    Tips.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_tips'</script>")
def chatt(request,u):
    request.session['head']="CHAT"
    # request.session['uuid'] = u
    # print("uuuuu", request.session['uuid'])
    return render(request,'Expert/expertchat.html',{'u':u})


def chatsnd(request,u):
        d=datetime.datetime.now().strftime("%Y-%m-%d")
        # t=datetime.datetime.now().strftime("%H:%M:%S")
        c = request.session['lid']
        b=request.POST['n']
        print(b)
        print(u,"userrrrrrrrrr")
        m=request.POST['m']
        cc = Expert.objects.get(LOGIN__id=c)
        uu = parent.objects.get(id=u)
        print("sssssss",uu)
        obj=chat()
        obj.date=d
        obj.type='expert'
        obj.EXPERT=cc
        obj.PARENT_id=uu.id
        obj.message=m
        obj.save()
        print(obj)
        v = {}
        if int(obj) > 0:
            v["status"] = "ok"
        else:
            v["status"] = "error"
        r = JsonResponse.encode(v)
        return r
    # else:
    #     return redirect('/')

def chatrply(request,u):
    # if request.session['log']=="lo":
        c = request.session['lid']
        cc=Expert.objects.get(LOGIN__id=c)
        # u=request.session['uuid']
        print("uid",u)
        uu=parent.objects.get(id=u)

        res = chat.objects.filter(EXPERT=cc,PARENT=uu)
        print(res)
        v = []
        if len(res) > 0:
            print(len(res))
            for i in res:
                v.append({
                    'type':i.type,
                    'chat':i.message,
                    'name':i.PARENT.name,
                    # 'upic':i.USER.photo,
                    'dtime':i.date,
                    'tname':i.EXPERT.name,
                })
            # print(v)
            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})
def expert_view_parent(request):
    data=parent.objects.filter(LOGIN__usertype='parent')
    return render(request,'Expert/view_parent.html',{'data':data})

# =================================STaff========================================================================================

def staff_home(request):
    return render(request,'staff/staff_home.html')

def view_staff_profile(request):
    data = Staff.objects.get(LOGIN=request.session['lid'])
    return render(request, 'staff/view_profile.html', {'data': data})

def add_student(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request,'staff/add_student.html')

def add_student_post(request):
    name=request.POST['textfield']
    plc=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    clas=request.POST['textfield5']
    div=request.POST['textfield6']
    gen=request.POST['RadioGroup1']
    dob=request.POST['textfield7']
    obj=Student()
    obj.name=name
    obj.place=plc
    obj.pin=pin
    obj.post=post
    obj.clas=clas
    obj.division=div
    obj.gender=gen
    obj.dob=dob
    obj.STAFF=Staff.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('added');window.location='/staff_home'</script>")


def view_staff_student(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Student.objects.filter(STAFF__LOGIN=request.session['lid'])
        return render(request, 'staff/view_student.html',{'data':data})

def edit_student(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Student.objects.get(id=id)
        return render(request, 'staff/edit_student.html',{'data':data})

def edit_student_post(request,id):
    name = request.POST['textfield']
    plc = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    clas = request.POST['textfield5']
    div = request.POST['textfield6']
    gen = request.POST['RadioGroup1']
    dob = request.POST['textfield7']
    Student.objects.filter(id=id).update(name=name,place=plc,post=post,pin=pin,clas=clas,division=div,gender=gen,dob=dob)
    return HttpResponse("<script>alert('edited');window.location='/view_staff_student'</script>")

def delete_student(request,id):
    Student.objects.get(id=id).delete()
    return HttpResponse("<script>alert('delete');window.location='/view_staff_student'</script>")

def view_work(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=work.objects.filter(STAFF__LOGIN=request.session['lid'])
        return render(request, 'staff/view_work.html',{'data':data})




def assign_work_student(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data = Student.objects.filter(STAFF__LOGIN=request.session['lid'])
        return render(request, 'staff/allocate_work.html', {'data': data,'wid':id})

def assign_work_student_post(request,id):
    std=request.POST['select']
    obj=assign_work()
    obj.WORK_id=id
    obj.STUDENT_id=std
    obj.status='allocated'
    obj.date=datetime.datetime.now().strftime('%Y-%m-%d')
    obj.save()
    return HttpResponse("<script>alert('assigned');window.location='/view_work'</script>")



def view_work_status(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data = assign_work.objects.filter(WORK__STAFF__LOGIN=request.session['lid'])
        return render(request, 'staff/view_work_status.html', {'data': data})


def add_note(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request, 'staff/add_note.html')

def add_note_post(request):
    note=request.POST['textarea']
    obj=work()
    obj.work=note
    obj.date=datetime.datetime.now().strftime('%Y-%m-%d')
    obj.STAFF=Staff.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('assigned');window.location='/staff_home'</script>")

def view_note(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=work.objects.filter(STAFF__LOGIN=request.session['lid'])
        return render(request, 'staff/view_note.html',{'data':data})

def edit_note(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=work.objects.get(id=id)
        return render(request, 'staff/edit_note.html',{'data':data})


def edit_note_post(request,id):
    note = request.POST['textarea']
    work.objects.filter(id=id).update(work=note)
    return HttpResponse("<script>alert('edited');window.location='/view_note'</script>")

def delete_note(request,id):
    work.objects.get(id=id).delete()
    return HttpResponse("<script>alert('delete');window.location='/view_note'</script>")

def staff_view_parent(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=parent.objects.filter(LOGIN__usertype='parent')
        return render(request, 'staff/view_parent.html',{'data':data})

def assign_child(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data = Student.objects.filter(STAFF__LOGIN=request.session['lid'])
        return render(request, 'staff/allocate_parent.html', {'data': data,'sid':id})

def assign_child_post(request,id):
    st=request.POST['select']
    data=childassign()
    data.STUDENT_id=st
    data.PARENT_id=id
    data.save()
    return HttpResponse("<script>alert('added');window.location='/staff_view_parent'</script>")

def add_student_performance(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request, 'staff/student_performance.html', {'sid': id})

def add_student_performance_post(request,id):
    pr=request.FILES['fileField']
    date=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    fs=FileSystemStorage()
    fs.save(r"C:\Users\Mottuz\student_track\media\image\\"+date+'.pdf',pr)
    path='/media/image/'+date+'.pdf'
    data=performance()
    data.STUDENT_id=id
    data.STAFF=Staff.objects.get(LOGIN=request.session['lid'])
    data.photo=path
    data.date=datetime.datetime.now().strftime('%Y-%m-%d')
    data.save()
    return HttpResponse("<script>alert('added');window.location='/view_staff_student'</script>")

def add_attendence(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request, 'staff/add_attendence.html', {'sid': id})

def add_attendence_post(request,id):
    at=request.POST['CheckboxGroup1']
    dat=attendence()
    dat.STUDENT_id=id
    dat.date=datetime.datetime.now().strftime('%Y-%m-%d')
    dat.status=at
    dat.save()
    return HttpResponse("<script>alert('added');window.location='/view_staff_student'</script>")

def add_student_note(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        return render(request, 'staff/student_note_add.html', {'sid': id})


def add_student_note_post(request):
    pr = request.FILES['fileField']
    date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(r"C:\Users\Mottuz\student_track\media\image\\" + date + '.pdf', pr)
    path = '/media/image/' + date + '.pdf'
    data = note()
    data.STAFF = Staff.objects.get(LOGIN=request.session['lid'])
    data.photo = path
    data.date = datetime.datetime.now().strftime('%Y-%m-%d')
    data.save()
    return HttpResponse("<script>alert('added');window.location='/staff_home'</script>")

def view_student_note(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=note.objects.filter(STAFF__LOGIN=request.session['lid'])
        return render(request, 'staff/view_student_note.html', {'data': data})

def delete_student_note(request,id):
    note.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_student_note'</script>")


# ============================Parent============================================================================================

def parent_home(request):
    return render(request,'parent/parentindex.html')

def parent_reg(request):
     return render(request,'parent/parent_register.html')
def parent_reg_post(request):
    name=request.POST['textfield']
    plc=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    emil=request.POST['textfield5']
    phn=request.POST['textfield6']
    dat=Login.objects.filter(username=emil)
    rd=random.randint(0000,9999)
    if dat.exists():
        return HttpResponse("<script>alert('the user already exists');window.location='/'</script>")
    else:
        log=Login()
        log.username=emil
        log.password=rd
        log.usertype='pending'
        log.save()

        reg=parent()
        reg.name=name
        reg.place=plc
        reg.post=post
        reg.pin=pin
        reg.email=emil
        reg.phone=phn
        reg.LOGIN=log
    #     gmail = smtplib.SMTP('smtp.gmail.com', 587)
    #
    #     gmail.ehlo()
    #
    #     gmail.starttls()
    #
    #     gmail.login('riss.athulchandran@gmail.com', 'cjcyiddroayvvpqn')
    #
    #     print("Couldn't setup email!!" + str(e))
    #
    #     msg = MIMEText("Your Password is " + str(rd))
    #
    #     msg['Subject'] = 'Verification'
    #
    #     msg['To'] = email
    #
    #     msg['From'] = 'riss.athulchandran@gmail.com'
    #
    # try:
    #
    #     gmail.send_message(msg)
    #
    # except Exception as e:
    #
    #     print("COULDN'T SEND EMAIL", str(e))
        reg.save()
        return HttpResponse("<script>alert('registred');window.location='/'</script>")

def parent_view_experts(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Expert.objects.all()
        return render(request, 'parent/view_expert.html', {'data':data})

def parent_view_tips(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=Tips.objects.filter(EXPERT=id)
        return render(request,'parent/view_tips.html',{'data':data})

def parent_view_student(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=childassign.objects.filter(PARENT__LOGIN=request.session['lid'])
        return render(request,'parent/view_student.html',{'data':data})

def view_student_work(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=assign_work.objects.filter(STUDENT=id)
        return render(request,'parent/view_work.html',{'data':data})


def update_work_status(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:

        return render(request, 'parent/update_work_status.html', {'id': id})

def update_work_status_post(request,id):
    st=request.POST['textarea']
    assign_work.objects.filter(id=id).update(status=st)
    return HttpResponse("<script>alert('updated success');window.location='/parent_view_student'</script>")

def student_performance(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=performance.objects.filter(STUDENT=id)
        return render(request,'parent/view_performance.html',{'data':data})

def student_attendence(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data=attendence.objects.filter(STUDENT=id)
        return render(request,'parent/view attendence.html',{'data':data})


def view_notification(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data = notification.objects.all()
        return render(request, 'parent/view_nofification.html', {'data': data})

def parent_view_note(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout success');window.location='/'</script>")
    else:
        data = note.objects.all()
        return render(request, 'parent/view_note.html', {'data': data})

def student_bus(request,id):
    data=Busassign_student.objects.get(STUDENT=id)
    bid=Busassign_student.objects.get(STUDENT=id).BUS_id
    did=Busassign_driver.objects.get(BUS=bid).DRIVER_id
    loc=locate.objects.get(DRIVER=did)
    return render(request,'parent/view_student_bus.html',{'data':data,"loc":loc})

def chattt(request,u):
        request.session['head'] = "CHAT"
        request.session['uid'] = u
        print("uidddddddddd",u)
        return render(request, 'parent/parentchat.html', {'u': u})

def chatsndd(request, u):
        d = datetime.datetime.now().strftime("%Y-%m-%d")
        # t=datetime.datetime.now().strftime("%H:%M:%S")
        c = request.session['lid']
        b = request.POST['n']
        print(b)
        print(u, "userrrrrrrrrr")
        m = request.POST['m']
        cc = parent.objects.get(LOGIN__id=c)
        # uu = Expert.objects.get(id=request.session['uid'])
        uu = Expert.objects.get(id=u)
        obj = chat()
        obj.date = d
        obj.type = 'parent'
        obj.PARENT = cc
        obj.EXPERT_id = uu.id
        obj.message = m
        obj.save()
        print(obj)
        v = {}
        if int(obj) > 0:
            v["status"] = "ok"
        else:
            v["status"] = "error"
        r = JsonResponse.encode(v)
        return r
        # else:
        #     return redirect('/')

def chatrplyy(request,u):
        # if request.session['log']=="lo":
        c = request.session['lid']
        cc = parent.objects.get(LOGIN__id=c)
        # uu = Expert.objects.get(id=request.session['uid'])
        uu = Expert.objects.get(id=u)
        res = chat.objects.filter(PARENT=cc, EXPERT=uu.id)
        print(res)
        v = []
        if len(res) > 0:
            print(len(res))
            for i in res:
                v.append({
                    'type': i.type,
                    'chat': i.message,
                    'name': i.PARENT.name,
                    # 'upic':i.USER.photo,
                    'dtime': i.date,
                    'tname': i.EXPERT.name,
                })
            # print(v)
            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})

def view_parent(request):
    data=parent.objects.all()
    return render(request,'Expert/view_parent.html',{'data':data})


# ===============Android===================================================================================================

def andro_log(request):
    username=request.POST['u']
    password = request.POST['p']
    alog=Login.objects.filter(username=username,password=password)
    if alog.exists():

        lid=alog[0].id
        type=alog[0].usertype

        return JsonResponse({'status':"ok",'type':type,'lid':lid})

    return JsonResponse({'status': "none"})

def andro_profile(request):
    lid = request.POST['lid']
    print(lid)
    qry=Driver.objects.get(LOGIN=lid)
    return JsonResponse({'status':"ok","username":qry.name,"exp":qry.experience,"lino":qry.licenseno,"email":qry.email,"phone":qry.phone})

def update_location(request):
    lid=request.POST['lid']
    lati=request.POST['lati']
    longi=request.POST['longi']
    obj=locate.objects.filter(DRIVER__LOGIN=lid)
    if obj.exists():
        locate.objects.filter(DRIVER__LOGIN=lid).update(lattitude=lati,longitude=longi)
        return JsonResponse({"status": "ok"})
    else:
        dat=locate()
        dat.DRIVER=Driver.objects.get(LOGIN=lid)
        dat.lattitude=lati
        dat.longitude=longi
        dat.save()
        return JsonResponse({"status":"ok"})

def andro_notification(request):
    lid = request.POST['lid']
    msg = request.POST['notification']
    dat=notification()
    dat.DRIVER=Driver.objects.get(LOGIN=lid)
    dat.notification=msg
    dat.date=datetime.datetime.now().strftime('%Y-%m-%d')
    dat.save()
    return JsonResponse({"status": "ok"})

def andro_view_bus(request):
    lid = request.POST['lid']
    qry=Busassign_driver.objects.get(DRIVER__LOGIN=lid)
    return JsonResponse({"status":"ok","busno":qry.BUS.vehicleno})

def andro_student_status(request):
    lid=request.POST['lid']
    sid=request.POST['sid']
    status=request.POST['status']
    dat=std_status()
    dat.DRIVER=Driver.objects.get(LOGIN=lid)
    dat.STUDENT=Student.objects.get(id=sid)
    dat.date=datetime.datetime.now().strftime('%Y-%m-%d')
    dat.status=status
    dat.save()
    return JsonResponse({"status": "ok"})


def andro_view_student(request):
    lid=request.POST['lid']
    bid=Busassign_driver.objects.get(DRIVER__LOGIN=lid).BUS_id
    data=Busassign_student.objects.filter(BUS=bid)
    ary=[]
    for i in data:
        ary.append({
            "id":i.STUDENT.id,
            "name":i.STUDENT.name,
            "plc":i.STUDENT.place,
            "cls":i.STUDENT.clas,
            "div":i.STUDENT.division,
            "gen":i.STUDENT.gender
        })
    return JsonResponse({"status":"ok","data":ary})

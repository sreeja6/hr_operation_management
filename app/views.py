from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.utils import IntegrityError
from app.models import Employee,recurt,ApplicantRegisteration,Applicant_Application_form,InterviewSchedule,Finalized_candiadates
def Home(request):
    return render(request,"home_page.html")
    print("home")
def admin_loginpage(request):
    return render(request,"admin_loginpage.html")
def admin_sucessfully_login(request):
    u = request.GET.get("a1")
    p = request.GET.get("a2")

    if u == "admin" and p == "admin":
        request.session['userA'] = u
        request.session['passdA'] = p
        return render(request,"admin_sucessfully_login.html")
    else:
        messages.error(request,"invalid Username OR Password")
        return redirect('admin_loginpage')
def add_emp_page(request):
    return render(request,"add_emp_page.html")
def add_emp_sucessfully(request):
    e_name = request.POST.get("e1")
    e_pass = request.POST.get("e2")
    e_des = request.POST.get("e3")
    e_add = request.POST.get("e4")
    e_con = request.POST.get("e5")
    e_ema = request.POST.get("e6")
    Employee(emp_name=e_name,emp_password=e_pass,emp_designation=e_des,emp_adress=e_add,emp_contact=e_con,emp_email=e_ema).save()
    messages.success(request,"One Employee is Added")
    return redirect('add_emp_page')
def view_emp_page(request):
    view_emp = Employee.objects.all()
    return render(request,"view_emp_page.html",{"view":view_emp})
def update_emp_page(request):
    update = Employee.objects.all()
    return render(request,"update_emp_page.html",{"up":update})
def go_upate_emp(request):
    n = request.GET.get('no')
    res = Employee.objects.get(emp_no=n)
    print(res)
    print(res.emp_name)
    return render(request,"lets_update_emp.html",{"update":res})
def updated_emp(request):
    u_no = request.POST.get("u1")
    u_name = request.POST.get("u2")
    u_pass = request.POST.get("u3")
    u_des = request.POST.get("u4")
    u_add = request.POST.get("u5")
    u_con = request.POST.get("u6")
    u_ema = request.POST.get("u7")
    Employee.objects.filter(emp_no=u_no) .update(emp_no=u_no, emp_name=u_name, emp_password=u_pass,
                                             emp_designation=u_des, emp_adress=u_add, emp_contact=u_con
                                             , emp_email=u_ema)
    return redirect('view_emp_page')

def delete_emp_page(request):
    de = Employee.objects.all()
    return render(request,"delete_emp_page.html",{"delete":de})
def deleted_emp(request):
    de = request.GET.get("d1")
    Employee.objects.filter(emp_no=de).delete()
    return redirect('view_emp_page')

def manager_loginpage(request):
    return render(request,"manager_loginpage.html")

def manager_sucessfully_login(request):
    mu = request.GET.get("m1")
    mp = request.GET.get("m2")
    if mu == "manager" and mp == "manager":
        request.session['u'] = mu
        request.session['p'] = mp
        return render(request, "manager_sucessfully_login.html")
    else:
        messages.error(request, "invalid Username OR Password")
        return redirect('manager_loginpage')
def recuritment_schedule(request):
    return render(request,"recuritment_schedule.html")
def interview_schedule(request):
    return render(request,"interview_schedule.html",{"ap":Applicant_Application_form.objects.values("id")})
def adding_new_recurt(request):
    return render(request,'adding_new_recurt.html')

def save_rect_details(request):
    c = request.POST.get("r1")
    q = request.POST.get("r2")
    sd = request.POST.get("r3")
    a = request.POST.get("r4")
    ld = request.POST.get("r5")
    di = request.POST.get("r6")
    p = request.POST.get("r7")
    de = request.POST.get("r8")
    re = request.POST.get("r9")
    cn = request.POST.get("r10")
    recurt(oppcode=c,quali=q,startdate=sd,age=a,lastdate=ld,deptid=di,position=p,des=de,res=re,cno=cn).save()
    return redirect('adding_new_recurt')
def view_all_rect(request):
    return render (request,"view_all_rect.html",{"rect":recurt.objects.all()})
def modify_recurt_det(request):
    return render(request,'modify_recurt_det.html',{'opp': recurt.objects.values('oppcode')})

def go_modify_rec_dt(request):
    opco = request.GET.get("rm")
    r = recurt.objects.get(oppcode=opco)
    return render(request,"lets_upadate_rect.html",{"update_rect":r})

def updated_rect(request):
    op = request.POST.get('p1')
    ql = request.POST.get('p2')
    s = request.POST.get('p3')
    ag = request.POST.get('p4')
    lsd = request.POST.get('p5')
    d = request.POST.get('p6')
    po = request.POST.get('p7')
    dis = request.POST.get('p8')
    res = request.POST.get('p9')
    ct = request.POST.get('p10')
    recurt.objects.filter(oppcode=op) .update(quali=ql,startdate=s,age=ag,lastdate=lsd,deptid=d,position=po,des=dis,res=res,cno=ct)
    return redirect('view_all_rect')
def delete_recurt_det(request):
    return render(request,"delete_recurt_det.html",{"d": recurt.objects.all()})
def lets_delete_rect(request):
    dr = request.GET.get('d')
    recurt.objects.get(oppcode=dr).delete()
    return redirect('view_all_rect')
def applicant_loginpage(request):
    return render(request,"applicant_loginpage.html")
def applicant_page(request):
    return render(request,"applicant_page.html")

def applicant_reg_page(request):
    return render(request,"applicant_reg_page.html")

def applicant_registeration_sucessfully(request):
    na = request.POST.get("e1")
    db = request.POST.get("e2")
    mail = request.POST.get("e3")
    gen = request.POST.get("e4")
    mobil = request.POST.get("e5")
    ad = request.POST.get("e6")
    uname = request.POST.get("e7")
    pas = request.POST.get("e8")
    try:
     ApplicantRegisteration(name=na,date_of_birth=db,email=mail,gender=gen,mobile_no=mobil,Adress=ad,username=uname,password=pas).save()
     return render(request,"applicant_register_failed.html",{'as':"sucessfully registered please login"})
    except IntegrityError:
        return render(request, "applicant_register_failed.html",{'af': "you are already registerd please login with ur username and password"})


def applicant_sucessfully_login(request):
    us = request.POST.get("a1")
    ps = request.POST.get("a2")
    try:
      request.session['us'] = us
      res = ApplicantRegisteration.objects.get(username=us,password=ps)
      rec = recurt.objects.values("quali","des")
      return render(request,"applicant_aplicationform.html",{"data": res,"ret": rec})
    except ApplicantRegisteration.DoesNotExist:
        messages.error(request,"Invalid login details")
        return redirect('applicant_loginpage')
def applicant_application_form(request):
    na = request.POST.get("e1")
    db = request.POST.get("e2")
    mail = request.POST.get("e3")
    gen = request.POST.get("e4")
    mobil = request.POST.get("e5")
    ad = request.POST.get("e6")
    qua = request.POST.get("e7")
    post = request.POST.get("e8")
    per = request.POST.get("e9")
    resume = request.FILES["e10"]
    try:
        Applicant_Application_form.objects.get(email=mail,post=post)
        return render(request, "aplicant_applied_sucessfully.html",{"af":"You already applied to this post"})
    except Applicant_Application_form.DoesNotExist:
      Applicant_Application_form(name=na,date_of_birth=db,email=mail,gender=gen,mobile_no=mobil,Adress=ad,qualifaction=qua,post=post,
                               percentage=per,resume=resume).save()
      return render(request, "aplicant_applied_sucessfully.html", {"as": "sucessfully you applied"})


def assign_interview_for_an_applocant(request):
    ai = request.POST.get("ai")
    return render(request,"assign_interview_for_an_applocant.html",{"id":ai,"empno":Employee.objects.values("emp_no")})


def save_applicant_interview_schedule(request):
    a_id = request.POST.get("i1")
    e_id = request.POST.get("i2")
    s_date = request.POST.get("i3")
    try:
        InterviewSchedule.objects.get(applicant_id=a_id)
        return render(request, "applicant_scheduled_tointerv_sucessfully.html",{"aif": "Applicant already Scheduled to the Interview"})
    except InterviewSchedule.DoesNotExist:
        InterviewSchedule(applicant_id=a_id, emp_id=e_id, schedule_date=s_date).save()
        return render(request, "applicant_scheduled_tointerv_sucessfully.html",{"ais" :"One applicant sucessfully Scheduled to the Interview"})


def intereviewer_login_page(request):
    return render(request,"intereviewer_login_page.html")
def interviwer_sucessfully_login(request):
    u = request.GET.get("a1")
    p = request.GET.get("a2")
    if u == "madhuri" and p == "madhuri":
        request.session["iu"] = u
        request.session["ip"] = p
        return render(request, "conducting_final_selection_last.html",{'aid':InterviewSchedule.objects.values('applicant_id')})
    else:
        messages.error(request, "invalid Username OR Password")
        return redirect('intereviewer_login_page')


def finilazing_candiadates(request):
    f_c = request.POST.get("cfinal")
    re = InterviewSchedule.objects.get(applicant_id=f_c)
    return render(request,"finilazing_candiadates.html",{"f":re})

def finalized_candiadates(request):
    i_id = request.POST.get("f1")
    a_id = request.POST.get("f2")
    s_d = request.POST.get("f3")
    res = request.POST.get("f4")
    try:
      Finalized_candiadates.objects.get(f_applicant_id=a_id)
      return render(request,"finalized_candidates_check.html",{"ff":"you are already finalized this applicant"})
    except IntegrityError:
      Finalized_candiadates(f_emp_id=i_id,f_applicant_id=a_id,f_schedule_date=s_d,result=res).save()
      return render(request, "finalized_candidates_check.html", {"fs": " you finalized one applicant sucessfully"})
    return None
def hr_login_page(request):
    return render(request,"hr_login_page.html")
def hr_sucessfully_login(request):
    u = request.GET.get("a1")
    p = request.GET.get("a2")
    s = Finalized_candiadates.objects.filter(result='Selected')
    r = Finalized_candiadates.objects.filter(result='Reject')
    st = Finalized_candiadates.objects.filter(result='Shorlisted')

    if u == "sree" and p == "sree":
        request.session["hu"] = u
        request.session["hp"] = p
        return render(request, "hr_sucessfully_login.html")
    else:
        messages.error(request, "invalid Username OR Password")
        return redirect('hr_login_page')
def selected_candiadates(request):
    se = Finalized_candiadates.objects.filter(result='Selected')
    l = []
    l1 = []
    print(se)
    for x in se:
        l.append(x.f_applicant_id)
    print(l)
    for x in l:
        l1.append(Applicant_Application_form.objects.get(id=x))
    print(l1)
    return render(request,"slelcted_candidates.html",{"sel": l1})
def rejected_candiadates(request):
    se = Finalized_candiadates.objects.filter(result='Reject')
    r = []
    r1 = []
    print(se)
    for x in se:
        r.append(x.f_applicant_id)
    print(r)
    for x in r:
        r1.append(Applicant_Application_form.objects.get(id=x))
    print(r1)
    return render(request, "rejected_candidates.html", {"rej": r1})

def shortlisted_candiadates(request):
    sr = Finalized_candiadates.objects.filter(result='Shorlisted')
    sl = []
    sl1 = []
    print(sl)
    for x in sr:
        sl.append(x.f_applicant_id)
    print(sl)
    for x in sl:
        sl1.append(Applicant_Application_form.objects.get(id=x))
    print(sl1)
    return render(request, "shortlisted_candidates.html", {"st": sl1})







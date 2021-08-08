"""hr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('admin_loginpage/',views.admin_loginpage,name="admin_loginpage"),
    path('admin_sucessfully_login/',views.admin_sucessfully_login,name="admin_sucessfully_login"),
    path('add_emp_page/',views.add_emp_page,name='add_emp_page'),
    path('add_emp_sucessfully/',views.add_emp_sucessfully,name='add_emp_sucessfully'),
    path('view_emp_page/',views.view_emp_page,name='view_emp_page'),
    path('update_emp_page/',views.update_emp_page,name='update_emp_page'),
    path('go_upate_emp/',views.go_upate_emp,name='go_upate_emp'),
    path('updated_emp/',views.updated_emp,name='updated_emp'),
    path('delete_emp_page/',views.delete_emp_page,name='delete_emp_page'),
    path('deleted_emp/',views.deleted_emp,name='deleted_emp'),
    path('manager_loginpage/',views.manager_loginpage,name='manager_loginpage'),
    path('manager_sucessfully_login/',views.manager_sucessfully_login,name='manager_sucessfully_login'),
    path('recuritment_schedule/',views.recuritment_schedule,name='recuritment_schedule'),
    path('interview_schedule/',views.interview_schedule,name='interview_schedule'),
    path('adding_new_recurt/',views.adding_new_recurt,name='adding_new_recurt'),
    path('save_rect_details/',views.save_rect_details,name='save_rect_details'),
    path('view_all_rect/',views.view_all_rect,name='view_all_rect'),
    path('modify_recurt_det/',views.modify_recurt_det,name='modify_recurt_det'),
    path('go_modify_rec_dt/',views.go_modify_rec_dt,name='go_modify_rec_dt'),
    path('updated_rect/',views.updated_rect,name='updated_rect'),
    path('delete_recurt_det/', views.delete_recurt_det, name='delete_recurt_det'),
    path('lets_delete_rect/', views.lets_delete_rect, name='lets_delete_rect'),


    path('applicant_loginpage/',views.applicant_loginpage,name='applicant_loginpage'),
    path('applicant_page/',views.applicant_page,name='applicant_page'),
    path('applicant_reg_page/',views.applicant_reg_page,name='applicant_reg_page'),
    path('applicant_registeration_sucessfully/',views.applicant_registeration_sucessfully,name='applicant_registeration_sucessfully'),
    path('applicant_sucessfully_login/',views.applicant_sucessfully_login,name='applicant_sucessfully_login'),
    path('applicant_Application_form/',views.applicant_application_form,name='applicant_application_form'),
    path('assign_interview_for_an_applocant/',views.assign_interview_for_an_applocant,name='assign_interview_for_an_applocant'),
    path('save_applicant_interview_schedule/',views.save_applicant_interview_schedule,name='save_applicant_interview_schedule'),
    path('intereviewer_login_page/',views.intereviewer_login_page,name='intereviewer_login_page'),
    path('interviwer_sucessfully_login/',views.interviwer_sucessfully_login,name='interviwer_sucessfully_login'),
    path('finilazing_candiadates/',views.finilazing_candiadates,name='finilazing_candiadates'),
    path('finalized_candiadates/',views.finalized_candiadates,name='finalized_candiadates'),
    path('hr_login_page/',views.hr_login_page,name='hr_login_page'),
    path('hr_sucessfully_login/',views.hr_sucessfully_login,name='hr_sucessfully_login'),
    path('selected_candiadates/',views.selected_candiadates,name='selected_candiadates'),
    path('rejected_candiadates/',views.rejected_candiadates,name='rejected_candiadates'),
    path('shortlisted_candiadates/',views.shortlisted_candiadates,name='shortlisted_candiadates')
]


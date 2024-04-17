"""student_track URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('login_post',views.login_post),
    path('admin_home',views.admin_home),
    path('logout',views.logout),
    path('add_expert',views.add_expert),
    path('add_expert_post',views.add_expert_post),
    path('view_expert',views.view_expert),
    path('edit_expert/<id>',views.edit_expert),
    path('edit_expert_post/<id>',views.edit_expert_post),
    path('delete_expert/<id>',views.delete_expert),
    path('add_staff',views.add_staff),
    path('add_staff_post',views.add_staff_post),
    path('view_staff',views.view_staff),
    path('edit_staff/<id>',views.edit_staff),
    path('edit_staff_post/<id>',views.edit_staff_post),
    path('delete_staff/<id>',views.delete_staff),
    path('add_bus',views.add_bus),
    path('add_bus_post',views.add_bus_post),
    path('view_bus',views.view_bus),
    path('delete_bus/<id>',views.delete_bus),
    path('add_driver',views.add_driver),
    path('add_driver_post',views.add_driver_post),
    path('view_driver',views.view_driver),
    path('edit_driver/<id>',views.edit_driver),
    path('edit_driver_post/<id>',views.edit_driver_post),
    path('delete_driver/<id>',views.delete_driver),
    path('assign_bus_todriver',views.assign_bus_todriver),
    path('assign_bus_todriver_post',views.assign_bus_todriver_post),
    path('view_student',views.view_student),
    path('allocate_bus/<id>',views.allocate_bus),
    path('allocate_bus_post/<id>',views.allocate_bus_post),
    path('view_parents',views.view_parents),
    path('approve_parent/<id>',views.approve_parent),
    path('reject_parent/<id>',views.reject_parent),

# ========================Expert========================================================================================
    path('expert_home',views.expert_home),
    path('view_profile',views.view_profile),
    path('add_tips',views.add_tips),
    path('add_tips_post',views.add_tips_post),
    path('view_tips',views.view_tips),
    path('edit_tips/<id>',views.edit_tips),
    path('edit_tips_post/<id>',views.edit_tips_post),
    path('delete_tips/<id>',views.delete_tips),
    path('chatt/<u>',views.chatt),
    path('chatsnd/<u>',views.chatsnd),
    path('chatrply/<u>',views.chatrply),
    path('expert_view_parent',views.expert_view_parent),


# ====================================Staff=============================================================================
    path('staff_home',views.staff_home),
    path('view_staff_profile',views.view_staff_profile),
    path('add_student',views.add_student),
    path('add_student_post',views.add_student_post),
    path('view_staff_student',views.view_staff_student),
    path('edit_student/<id>',views.edit_student),
    path('edit_student_post/<id>',views.edit_student_post),
    path('delete_student/<id>',views.delete_student),
    path('view_work',views.view_work),
    path('assign_work_student/<id>',views.assign_work_student),
    path('assign_work_student_post/<id>',views.assign_work_student_post),
    path('view_work_status',views.view_work_status),
    path('add_note',views.add_note),
    path('add_note_post',views.add_note_post),
    path('view_note',views.view_note),
    path('edit_note/<id>',views.edit_note),
    path('edit_note_post/<id>',views.edit_note_post),
    path('delete_note/<id>',views.delete_note),
    path('staff_view_parent',views.staff_view_parent),
    path('assign_child/<id>',views.assign_child),
    path('assign_child_post/<id>',views.assign_child_post),
    path('add_student_performance/<id>',views.add_student_performance),
    path('add_student_performance_post/<id>',views.add_student_performance_post),
    path('add_attendence/<id>',views.add_attendence),
    path('add_attendence_post/<id>',views.add_attendence_post),
    path('add_student_note',views.add_student_note),
    path('add_student_note_post',views.add_student_note_post),
    path('view_student_note',views.view_student_note),
    path('delete_student_note/<id>',views.delete_student_note),


# ===================================parent=================================================================================
    path('parent_home',views.parent_home),
    path('parent_reg',views.parent_reg),
    path('parent_reg_post',views.parent_reg_post),
    path('parent_view_experts',views.parent_view_experts),
    path('parent_view_tips/<id>',views.parent_view_tips),
    path('parent_view_student',views.parent_view_student),
    path('view_student_work/<id>',views.view_student_work),
    path('update_work_status/<id>',views.update_work_status),
    path('update_work_status_post/<id>',views.update_work_status_post),
    path('parent_view_note',views.parent_view_note),
    path('student_performance/<id>',views.student_performance),
    path('student_attendence/<id>',views.student_attendence),
    path('view_notification',views.view_notification),
    path('chattt/<u>',views.chattt),
    path('chatsndd/<u>',views.chatsndd),
    path('chatrplyy/<u>',views.chatrplyy),
    path('student_bus/<id>',views.student_bus),

    # =============================================================================

    path('andro_log',views.andro_log),
    path('andro_profile',views.andro_profile),
    path('update_location',views.update_location),
    path('andro_notification',views.andro_notification),
    path('andro_view_bus',views.andro_view_bus),
    path('andro_student_status',views.andro_student_status),
    path('andro_view_student',views.andro_view_student),


   ]
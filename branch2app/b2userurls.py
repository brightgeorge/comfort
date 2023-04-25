from django.contrib import admin
from django.urls import path, include

from django.urls import path
from . import views
from . import admin_branch2

from . import branch1
from . import branch2


d='test'

import myapp.userurls
import branch2app.b2userurls
name='_branch2'
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('pysql/', branch1.pysql, name='pysql' + d),

    #path('viewall_vacate_guest/',branch1.viewall_vacate_guest,name='viewall_vacate_guest'+name),
    #path('view_all_users/', views.view_all_users, name='view_all_users'),
    #path('view_all_room/', admin_branch2.view_all_room, name='view_all_room'),

#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi/',admin_branch2.branch1_room_create_regi,name='branch1_room_create_regi'+name),
    path('view_all_room/',admin_branch2.view_all_room,name='view_all_rooms'+name),
    path('delete_room/<id>',admin_branch2.delete_room,name='delete_room'+name),

    path('branch1_room_create/',admin_branch2.branch1_room_create,name='branch1_room_create'+name),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi/', admin_branch2.pg1_bed_create_regi, name='pg1_bed_create_regi'+name),
    path('pg1_view_all_beds/', admin_branch2.pg1_view_all_beds, name='pg1_view_all_beds'+name),
    # path('delete_room/<id>', views.delete_room, name='delete_room'),

    path('pg1_bed_create/', admin_branch2.pg1_bed_create, name='pg1_bed_create'+name),

#bed creation end here

#guest
    path('br1_admit_guest/<id>',branch2.br1_admit_guest,name='br1_admit_guest'+name),
    path('view_all_new_guest/',branch2.view_all_new_guest,name='view_all_new_guest'+name),
    path('update_br1_admit_guest/<id>',branch2.update_br1_admit_guest,name='update_br1_admit_guest'+name),
    path('vacate_br1_guest/<id>',branch2.vacate_br1_guest,name='vacate_br1_guest'+name),
    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
#guest end here

]
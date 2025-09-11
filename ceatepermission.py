import code
from django.contrib.auth.models import Permission, Group





# création ou récupération des groups 

admin = Group.objects.get_or_create(name="admin")
validator = Group.objects.get_or_create(name="validator")
user = Group.objects.get_or_create(name="user")
  

admin_permission = [
    "add_user","view_user","delete_user","view_user",
    "add_mot","view_mot",
    "view_langue",
    "view_proposition"
]

for permission in admin_permission : 
    perm = Permission.object.get(codename=permission)
    admin.permissions.add(perm)
    


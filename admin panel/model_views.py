from flask_admin.contrib import sqla
from flask_security import current_user
from flask import redirect, url_for, request




class MyModelView(sqla.ModelView):
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('superuser') :
            return True
        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users
          when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class usernameview(MyModelView):
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('superuser') or current_user.has_role('user') :
    
            if current_user.has_role('user'):
                self.can_create = False
                self.can_edit = False
                self.can_delete = False
                self.can_export = False
                print('working User')
                
            elif current_user.has_role('superuser'):
                self.can_create = True
                self.can_edit = True
                self.can_delete = True
                self.can_export = True
                print('working Superuser')
                
            return True
        return False
            
        
    column_list=('id', 'first_name','last_name','username','email','active','roles','confirmed_at')



class testUserView(MyModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('superuser') or current_user.has_role('user') :
            return True
        return False
    
    column_display_pk = True
    form_columns = ['id', 'desc']
    column_searchable_list = ['desc']
    column_filters = ['id']
    can_create = True
    can_edit = True
    can_delete = False  # disable model deletion
    can_view_details = True
    page_size = 2  # pagination
    create_modal = True
    edit_modal = True
    can_export = True

class testAdminView(MyModelView):
    column_display_pk = True
    form_columns = ['id', 'desc']
    column_searchable_list = ['desc']
    column_filters = ['id']
    column_editable_list = ['desc']
    can_create = True
    can_edit = True
    
    can_delete = True
    can_view_details = True
    page_size = 2
    create_modal = True
    edit_modal = True
    can_export = True


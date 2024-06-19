from rest_framework import permissions
#permissão global, lógica default...
class GlobalDefaultPermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method, 
            view=view,
        )
        #Se caso for retornado None, null, ENTÃO NÃO PERMITA O ACESSO
        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)
    
     #f'{app_name}.{action_name}_{model_name}' -> padrão a ser usado na has_perm, e precisamos descobrir onde capturar esses dados
    def __get_model_permission_codename(self, method, view):
        try:   
            #buscar o model name -> nome do modelo ex: genres
            model_name = view.queryset.model._meta.model_name
            #descobrir o app atraves da view
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None
        
        
    def __get_action_sufix(self, method):
        method_actions = {
            'GET':'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }

        return method_actions.get(method, '')
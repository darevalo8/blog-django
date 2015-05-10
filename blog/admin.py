from django.contrib import admin
from .models import Categorie, UserProfile, Post, Comment


admin.site.register(Categorie)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # el campo list_display sirve para añadir mas elementos a la lista de cambios en el admin
    #si miran bien en el userprofile solo se veia el user, ahora con el
    #list_display se ven user, first_name, last_name :D
    list_display = ('user', 'first_name', 'last_name')
    #con el campo search_fields nos crea un formulario de busqueda que filtrara por
    #lo parametros que le mandemos en la tupla en este caso buscara por first_name y last_name :D
    search_fields = ('first_name', 'last_name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'fecha')
    #usamos list_filter, la cual es una tupla de campos que se usa para crear filtros a lo
    #largo de la barra lateral, del lado derecho de la lista de cambios. Para los campos de
    #fechas Django provee algunos atajos para filtrar las listas, tal como ‘‘Hoy’’, ‘‘Últimos 7
    #días’’, ‘‘Este mes’’ y ‘‘Este año
    list_filter = ('fecha',)
    #no cogee el date_hierar
    #date_hierarchy = 'fecha'
    ordering = ('-fecha',)
    fields = ('title', 'category', 'content', 'user', 'fecha')
    #este filter_horizontal solo sirve con campo de relacion de muchos a muchos
    #filter_horizontal = ()
    #el raq_id_fields nos permite quitar la combo box de los foreingkey y nos muestra un formulario
    #el cual se le asigna la clave primaria y listo
    #raw_id_fields = ('category',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

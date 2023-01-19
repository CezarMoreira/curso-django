from django.contrib import admin
from . models import Categoria, Contato

"""
http://turing.com.br/material/acpython/mod3/django/admin1.html
link com mais opçoes de formatação
"""



class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')
    

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

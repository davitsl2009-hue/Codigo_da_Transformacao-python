# produtos/admin.py

from django.contrib import admin


from .models import Produto


@admin.register(Produto)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade')
    
    search_fields = ('nome',)

'''
admin
admin@mail.com
@Zaq123123
'''
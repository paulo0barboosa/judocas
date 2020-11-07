from django.urls import path
from django.conf.urls import url, include
from .views import (
    home,
    cadastra_filiado,
    cadastra_professor,
    cadastra_academia,
    search_pessoa,
    search_academia,
    update_pessoa,
    update_academia,
    delete_pessoa,
    delete_academia,
    load_professores,
    load_professores_update
)


urlpatterns = [
    url(r'^home/$', home, name='core_home'), # home
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^cadastra_filiado/$', cadastra_filiado, name='core_cadastra_filiado'), # CADASTRO
    url(r'^cadastra_professor/$', cadastra_professor, name='core_cadastra_professor'), # CADASTRO
    url(r'^cadastra_academia/$', cadastra_academia, name='core_cadastra_academia'), # CADASTRO
    url(r'^update_pessoa/(?P<RegistroCBJ>\d+)/$', update_pessoa, name='core_update_pessoa'), # UPDATE
    url(r'^update_academia/(?P<IDAcademia>\d+)/$', update_academia, name='core_update_academia'), # UPDATE
    path('search_pessoa/', search_pessoa.as_view(), name='search_pessoa'), # SEARCH
    path('search_academia/', search_academia.as_view(), name='search_academia'), # SEARCH
    url(r'^delete_pessoa/(?P<RegistroCBJ>\d+)/$', delete_pessoa, name='core_delete_pessoa'), # DELETE
    url(r'^delete_academia/(?P<IDAcademia>\d+)/$', delete_academia, name='core_delete_academia'), # DELETE
    path('ajax/load_professores/', load_professores, name='ajax_load_professores'), # listagem de professores de acordo com a academia selecionada
    path('ajax/load_professores_update/', load_professores_update, name='ajax_load_professores_update'), # listagem de professores de acordo com a academia selecionada
]

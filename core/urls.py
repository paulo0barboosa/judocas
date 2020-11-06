from django.urls import path
from django.conf.urls import url, include
from .views import (
    home,
    # filiados_cadastrados,
    cadastra_filiado,
    # professores_cadastrados,
    cadastra_professor,
    # academias_cadastrados,
    cadastra_academia,
    search_pessoa,
    search_academia,
    update_pessoa,
    update_academia,
    delete_pessoa,
    delete_academia,
    load_professores
)


urlpatterns = [
    url(r'^home/$', home, name='core_home'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^cadastra_filiado/$', cadastra_filiado, name='core_cadastra_filiado'),
    url(r'^cadastra_professor/$', cadastra_professor, name='core_cadastra_professor'),
    url(r'^cadastra_academia/$', cadastra_academia, name='core_cadastra_academia'),
    url(r'^update_pessoa/(?P<RegistroCBJ>\d+)/$', update_pessoa, name='core_update_pessoa'),
    url(r'^update_academia/(?P<IDAcademia>\d+)/$', update_academia, name='core_update_academia'),
    path('search_pessoa/', search_pessoa.as_view(), name='search_pessoa'),
    path('search_academia/', search_academia.as_view(), name='search_academia'),
    url(r'^delete_pessoa/(?P<RegistroCBJ>\d+)/$', delete_pessoa, name='core_delete_pessoa'),
    url(r'^delete_academia/(?P<IDAcademia>\d+)/$', delete_academia, name='core_delete_academia'),

    path('ajax/load_professores/', load_professores, name='ajax_load_professores'),
    # url(r'^professores/$', professores_cadastrados, name='core_professores_cadastrados'),
    # url(r'^academias/$', academias_cadastrados, name='core_academias_cadastrados'),
    # url(r'^filiados/$', filiados_cadastrados, name='core_filiados_cadastrados'),
]

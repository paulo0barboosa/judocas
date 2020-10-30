from django.urls import path
from django.conf.urls import url, include
from .views import (
    home,
    filiados_cadastrados,
    cadastra_filiado,
    professores_cadastrados,
    cadastra_professor,
    academias_cadastrados,
    cadastra_academia,
    search_pessoa,
    search_academia,
    update_pessoa,
    update_academia
)


urlpatterns = [
    url(r'^home/$', home, name='core_home'),
    url(r'^cadastra_filiado/$', cadastra_filiado, name='core_cadastra_filiado'),
    url(r'^filiados/$', filiados_cadastrados, name='core_filiados_cadastrados'),
    url(r'^cadastra_professor/$', cadastra_professor, name='core_cadastra_professor'),
    url(r'^update_pessoa/(?P<RegistroCBJ>\d+)/$', update_pessoa, name='core_update_pessoa'),
    url(r'^update_academia/(?P<IDAcademia>\d+)/$', update_academia, name='core_update_academia'),
    path('search_pessoa/', search_pessoa.as_view(), name='search_pessoa'),
    path('search_academia/', search_academia.as_view(), name='search_academia'),
    url(r'^professores/$', professores_cadastrados, name='core_professores_cadastrados'),
    url(r'^cadastra_academia/$', cadastra_academia, name='core_cadastra_academia'),
    url(r'^academias/$', academias_cadastrados, name='core_academias_cadastrados'),
    path('accounts/', include('django.contrib.auth.urls')),
]

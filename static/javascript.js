$("#id_CEP").focusout(function(){
    //Início do Comando AJAX
    $.ajax({
        //O campo URL diz o caminho de onde virá os dados
        //É importante concatenar o valor digitado no CEP
        url: 'https://viacep.com.br/ws/'+$(this).val()+'/json/unicode/',
        //Aqui você deve preencher o tipo de dados que será lido,
        //no caso, estamos lendo JSON.
        dataType: 'json',
        //SUCESS é referente a função que será executada caso
        //ele consiga ler a fonte de dados com sucesso.
        //O parâmetro dentro da função se refere ao nome da variável
        //que você vai dar para ler esse objeto.
        success: function(resposta){
            //Agora basta definir os valores que você deseja preencher
            //automaticamente nos campos acima.
            $("#id_Rua").val(resposta.logradouro);
            $("#id_Bairro").val(resposta.bairro);
            $("#id_Cidade").val(resposta.localidade);
            $("#id_Estado").val(resposta.uf);
            $("#id_Complemento").val(resposta.complemento);
            //Vamos incluir para que o Número seja focado automaticamente
            //melhorando a experiência do usuário
            $("#id_Numero").focus();
        }
    });
});

$(document).ready(function() {
    $('#id_Academia').change(function() {
      var filter = $(this).val();
      $('#id_Professor > option').each(function() {
        if ($(this).val() == filter) {
          $(this).show();
        } else {
          $(this).hide();
        }
        $('select').val(filter);
      })
    })
  })
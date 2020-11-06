$(document).ready(function() {
  $("#id_CEP").focusout(function(){ // mascara para campos de CEP
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
    
  var behavior = function (val) { // mascara de telefone
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00000';
  },
  options = {
    onKeyPress: function (val, e, field, options) {
        field.mask(behavior.apply({}, arguments), options);
    }
  };

  $('#id_Telefone1').mask(behavior, options);
  $('#id_Telefone2').mask(behavior, options);
})
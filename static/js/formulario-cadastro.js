let tel = '+5511983510940'
let message = ''
let wppUrl = ''

function createUrl() {
  var primeiro_nome = document.querySelector("#validationDefault01").value
  var sobrenome = document.querySelector("#validationDefault02").value
  var usuario = document.querySelector("#validationDefaultUsername").value
  var cidade = document.querySelector("#validationDefault03").value
  var estado = document.querySelector("#validationDefault04").value
  var cep = document.querySelector("#validationDefault05").value


  message = `*Primeiro Nome*: ${primeiro_nome},
             *Sobrenome*: ${sobrenome},
             *Nome de Usuário*: ${usuario},
             *Cidade*: ${cidade},
             *Estado*: ${estado},
             *Cep*: ${cep},
             `

  var messageUri = encodeURI(message)
  wppUrl =
    'https://api.whatsapp.com/send?phone=' + tel + '&text=' + messageUri

  var a = document.createElement('a')

  a.href = wppUrl
  a.target = '_blank'

  a.click()
}
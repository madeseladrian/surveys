## SignUpController

> ### Caso de sucesso

1. ✅ Chama o **Validation** com os valores **nome**, **email**, **password** e **password_confirmation** corretos
2. ✅ Chama o **AddAccount** com os valores **nome**, **email**, **password** corretos
3. ✅ **Adiciona** o usuário com o **nome**, **email** e **password** no banco de dados
4. ❌ **Busca** o usuário com o **email** e **password** fornecidos
5. ❌ Retorna **200** com o **token** de acesso

> ### Exceções

6. ✅ Retorna erro **400 - BadRequest** se o campo email for um email inválido
7. ✅ Retorna erro **403 - Forbidden** se encontrar um usuário com os dados fornecidos
8. ✅ Retorna erro **500 - ServerError** se der erro ao tentar validar as credenciais
9. ✅ Retorna erro **500 - ServerError** se der erro ao tentar adicionar o usuário
10.❌ Retorna erro **500 - ServerError** se der erro ao tentar gerar o token de acesso

### [Back](../../../readme.md)
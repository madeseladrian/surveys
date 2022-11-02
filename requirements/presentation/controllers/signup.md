## SignUpController

> ### Caso de sucesso

1. ✅ Valida os dados obrigatórios **nome**, **email** e **password**
2. ✅ **Adiciona** o usuário com o **nome**, **email** e **password** no banco de dados
3. ❌ **Busca** o usuário com o **email** e **password** fornecidos
4. ❌ Retorna **200** com o **token** de acesso

> ### Exceções

5. ✅ Retorna erro **400 - BadRequest** se o campo email for um email inválido
6. ✅ Retorna erro **403 - Forbidden** se encontrar um usuário com os dados fornecidos
7. ✅ Retorna erro **500 - ServerError** se der erro ao tentar validar as credenciais
8. ✅ Retorna erro **500 - ServerError** se der erro ao tentar adicionar o usuário
9. ❌ Retorna erro **500 - ServerError** se der erro ao tentar gerar o token de acesso

### [Back](../../../readme.md)
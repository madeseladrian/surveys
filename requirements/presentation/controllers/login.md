# Login

> ## Caso de sucesso

1. ❌ Chama o **Validation** com os valores **email** e **password** corretos
2. ❌ Chama o **Authentication** com os valores **email** e **password** corretos
3. ❌ **Busca** o usuário com o email e senha fornecidos
4. ❌ Retorna **200** com o token de acesso

> ## Exceções

5. ❌ Retorna erro **400 - BadRequest** se o campo email for um email inválido
6. ❌ Retorna erro **401 - Unauthorized** se não encontrar um usuário com os dados fornecidos
7. ❌ Retorna erro **500 - ServerError** se der erro ao tentar validar as credenciais
8. ❌ Retorna erro **500 - ServerError** se der erro ao tentar gerar o token de acesso

### [Back](../../../readme.md)
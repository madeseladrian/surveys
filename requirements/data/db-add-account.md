## DbAddAccount

> ### Caso de sucesso

1. ✅ **Chamar** o método com o **email** correto
2. ✅ **Verifica** se o **email** não está cadastrado
3. ✅ **Criptografar** o **password** chamando o **Hasher**
4. ✅ Retorna **True** caso a conta seja criada com sucesso

> ### Exceções

5. ❌ Retorna **False** se o **email** está cadastrado
6. ❌ Retorna **False** caso a conta não seja criada com sucesso
7. ❌ Retorna erro se der erro ao tentar validar o email
8. ❌ Retorna erro se der erro ao tentar encriptar a senha
9. ❌ Retorna erro se der erro ao tentar criar a conta
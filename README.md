

---

# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python. Ele permite realizar operações bancárias básicas, como depósito, saque, exibição de extrato, cadastro de novos clientes e contas. O sistema utiliza orientação a objetos (POO) para uma estrutura mais modular e organizada.

## Funcionalidades

- **Depositar:** Permite realizar depósitos na conta.
- **Sacar:** Permite realizar saques da conta, com verificação de saldo.
- **Exibir Extrato:** Exibe o extrato da conta com todas as transações realizadas.
- **Cadastrar Nova Conta:** Permite o cadastro de novas contas para clientes existentes.
- **Listar Contas:** Lista todas as contas cadastradas no sistema.
- **Novo Usuário:** Permite o cadastro de novos clientes no sistema.

## Estrutura do Código

### Classes

- **Histórico**
  - Armazena o histórico de transações de uma conta.
- **Transação**
  - Classe base para transações, com subclasses `Deposito` e `Saque`.
- **Conta**
  - Representa uma conta bancária genérica.
- **ContaCorrente**
  - Subclasse de `Conta` com limite de saque.
- **Cliente**
  - Armazena informações do cliente e suas contas.
- **PessoaFisica**
  - Subclasse de `Cliente` com informações específicas de pessoa física.

### Métodos Principais

- **menu():**
  - Exibe o menu principal e captura a escolha do usuário.
- **sacar(clientes):**
  - Realiza uma operação de saque em uma conta do cliente.
- **depositar(clientes):**
  - Realiza uma operação de depósito em uma conta do cliente.
- **exibir_extrato(clientes):**
  - Exibe o extrato de uma conta do cliente.
- **cadastrar_cliente(clientes):**
  - Cadastra um novo cliente.
- **cadastrar_conta(clientes, contas):**
  - Cadastra uma nova conta para um cliente existente.
- **listar_contas(contas):**
  - Lista todas as contas cadastradas.
- **filtrar_cliente(cpf, clientes):**
  - Filtra e retorna um cliente pelo CPF.
- **main():**
  - Função principal que controla o fluxo do programa.

## Como Usar

### Pré-requisitos

- Python 3.x instalado no seu sistema.

### Execução

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/sistema-bancario-python.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd sistema-bancario-python
    ```

3. Execute o script principal:
    ```sh
    python sistema_bancario.py
    ```

### Exemplo de Uso

Ao executar o script, o menu principal será exibido, permitindo escolher uma das opções disponíveis:

```
=========== MENU ============
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Cadastrar nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=> 
```

Escolha a opção desejada digitando a letra correspondente e siga as instruções fornecidas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

1. Faça um fork do projeto.
2. Crie uma nova branch com a sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -m 'Minha nova feature'`.
4. Faça push para a branch: `git push origin minha-feature`.
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.

---

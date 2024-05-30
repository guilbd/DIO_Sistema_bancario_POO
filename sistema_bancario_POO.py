import textwrap
from datetime import date

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

class Transacao:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses")

class Deposito(Transacao):
    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def registrar(self, conta):
        conta.sacar(self.valor)

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            self._historico.adicionar_transacao(f"Saque: {valor}")
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(f"Depósito: {valor}")
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self._limite = 1000.0
        self._limite_saques = 3

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

def menu():
    menu = """
    ============ MENU ============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Cadastrar nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui contas!")
        return None
    # FIXME: não permite cliente escolher a conta. Considera sempre a primeira
    return cliente.contas[0]

def sacar(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = float(input("Digite o valor do saque: "))
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Conta não encontrada!")
        return
    
    cliente.realizar_transacao(conta, transacao)

def depositar(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = float(input("Digite o valor do depósito: "))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Conta não encontrada!")
        return
    
    cliente.realizar_transacao(conta, transacao)
    
def exibir_extrato(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Conta não encontrada!")
        return
    
    print("\n==============EXTRATO==============")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações!"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao}"
            
    print(extrato)
    print(f"\nSaldo:\n\t R$ {conta.saldo:.2f}\n")        
    print("=======================================")

def cadastrar_cliente(clientes):
    cpf = input("Digite o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("Já existe cliente com esse CPF!")
        return
    
    nome = input("Digite o nome do cliente: ")
    dt_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço [logradouro, nº, bairro, cidade/estado]: ")
    
    novo_cliente = PessoaFisica(endereco, cpf, nome, dt_nascimento)
    clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")

def cadastrar_conta(clientes, contas):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        numero_conta = len(contas) + 1
        nova_conta = ContaCorrente(cliente, numero_conta)
        cliente.adicionar_conta(nova_conta)
        contas.append(nova_conta)
        print("Conta cadastrada com sucesso!")
    else:
        print("Cliente não encontrado!")

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Cliente: {conta.cliente.nome}")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nc':
            cadastrar_conta(clientes, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'nu':
            cadastrar_cliente(clientes)
        elif opcao == 'q':
            break
        else:
            print("Opção inválida!")

main()

# Sistema Bancário Simples

Este é um sistema bancário simples desenvolvido em Python. Ele permite ao usuário realizar operações básicas como depositar, sacar e visualizar o extrato.

## Funcionalidades

- **Depósito**: Permite adicionar um valor ao saldo bancário.
- **Saque**: Permite retirar um valor do saldo, respeitando o limite de saque por operação e a quantidade máxima de saques por sessão.
- **Extrato**: Exibe todas as transações realizadas e o saldo atual.
- **Sair**: Encerra o programa.

## Requisitos

- Python 3.x instalado

## Como Executar

```bash
# Clone este repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Navegue até o diretório do projeto
cd seu-repositorio

# Execute o script
python bank_system.py
```

## Uso

Ao iniciar o programa, um menu interativo será exibido. Basta selecionar a opção desejada digitando o número correspondente.

## Regras do Sistema

- O saldo inicial é de **R\$ 0,00**.
- O limite de saque é de **R\$ 500,00** por operação.
- O usuário pode realizar no máximo **3 saques** por sessão.
- Apenas valores **positivos** podem ser depositados ou sacados.

## Licença

Este projeto é de uso livre para estudo e aprimoramento pessoal.


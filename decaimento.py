import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import os
from termcolor import colored
from time import sleep




def grafico(n_vals, V_vals, limite):
    plt.ion()
    plt.plot(n_vals, V_vals, marker='o')
    plt.axhline(float(limite), color='red', linestyle='--',
                label=f"Limite = {limite}")
    plt.title("Decaimento do Valor do Ativo e Seu Limite (Cálculo Simbólico)")
    plt.xlabel("Tempo (n)")
    plt.ylabel("Valor V(n)")
    plt.grid(True)
    plt.legend()
    plt.show()
    plt.pause(0.001)
    input(colored("Aperte 'Enter' para fechar gráfico", 'green'))

    plt.close()

    return 0

def print_decaimento(n_vals, V_vals, limite, V0, r):
    print(colored("\nDECAIMENTO DO VALOR DO ATIVO", 'magenta', attrs=['bold']))
    print(colored("\nFÓRMULA DA FUNÇÃO:", 'green'))
    print(colored(f"V(n) = {V0} * (1 - {r})^n", 'yellow'))

    print(colored("\nCÁLCULO DO LIMITE (via SymPy):", 'green'))
    print(colored(f"lim (n→∞) V(n) = {limite}", 'yellow'))

    print(colored("\nVALORES CALCULADOS:", 'green'))
    for i in range(len(n_vals)):
        sleep(1)
        print(colored(f"Ano {int(n_vals[i])}", 'cyan') + ':' + f"R$ {V_vals[i]:.2f}")


def entrada_dados():
    while True:
        try:
            valor = float(input(">> "))
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print(colored("Entrada inválida. Certifique-se de que o valor seja numérico e maior que zero.", 'red'))
            sleep(2)

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():

    while True:
        limpar_tela()

        print(colored("MODELO DE DECAIMENTO DE UM ATIVO", "magenta", attrs=["bold"]) + colored("USANDO LIMITES (SYMPY)\n", "cyan"))

        print(colored("Digite os valores solicitados\n", 'green'))
        try:
            print(colored("Digite o valor inicial do ativo: ", 'yellow'))
            V0 = entrada_dados()

            print(colored("Digite a taxa de decaimento (entre 0 e 1): ", 'yellow'))
            r = entrada_dados()
            if not (0 < r < 1):
                raise ValueError("Taxa precisa estar entre 0 e 1.")

            print(colored("Digite por quantos períodos deseja simular: ", 'yellow'))
            n_max = entrada_dados()


        except Exception:
            sleep(2)
            continue
        
        limpar_tela()

        #reigon Calculos 

        # Variável simbólica
        n = sp.Symbol('n', real=True, positive=True)

        # Função simbólica do valor do ativo
        Vn = V0 * (1 - r)**n

        # Cálculo simbólico do limite
        limite = sp.limit(Vn, n, sp.oo)

        # Sequência numérica para o gráfico
        n_vals = np.arange(0, n_max + 1)
        V_vals = V0 * (1 - r)**n_vals

        #endregion

        print_decaimento(n_vals, V_vals, limite, V0, r)
        print(colored("\nVocê deseja ver o gráfico deste decaimento? [S/N]", 'yellow'))
        resposta = input(">> ").lower()

        if resposta == 'n': pass
        else: grafico(n_vals, V_vals, limite)


        nd = input(colored("Aperte 'Enter' para iniciar um novo decaimento", 'green'))

        if nd == '': continue
        else: break
main()

<div align="center">

  <img src="./graph/Meu.png" alt="Banner do Projeto" width="100%" />

  <h1>📉 Modelo de Decaimento de Ativo Usando Limites (Python + SymPy)</h1>

  <!-- BADGES -->
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Matplotlib-Graph-darkgreen?logo=plotly" />
  <img src="https://img.shields.io/badge/SymPy-Symbolic%20Math-orange" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />

  <p>
    Um projeto acadêmico que utiliza <strong>cálculo de limites</strong> aplicado ao 
    <strong>modelo de decaimento de valor de um ativo</strong>.  
    Inclui interface via terminal, validação de entrada, renderização gráfica interativa
    e cálculo simbólico via <strong>SymPy</strong>.
  </p>
</div>

---

## 📘 Sobre o Projeto

Este projeto implementa um **modelo matemático de decaimento exponencial**, onde um ativo perde valor ao longo do tempo conforme uma taxa de decaimento `r`.  
O cálculo do limite é realizado usando **SymPy**, garantindo que o conceito matemático seja aplicado no código — como exigido por atividades acadêmicas envolvendo limites.

O limite do modelo:

  lim_{`n` -> infty} `V(n)` = `V0` \cdot (1 - r)^`n` = 0

Onde:

- `V0` → valor inicial do ativo  
- `r` → taxa de decaimento  
- `n` → período  

---

## 🧮 Funcionalidades

- ✔ Entrada validada para evitar erros do usuário  
- ✔ Cálculo simbólico do limite usando **SymPy**  
- ✔ Impressão animada dos valores ano a ano  
- ✔ Gráfico interativo com Matplotlib  
- ✔ Fechamento manual da janela de gráfico  
- ✔ Interface colorida com `termcolor`  
- ✔ Limpeza da tela dinâmica (Windows ou Linux)  
- ✔ Loop para simular múltiplos decaimentos  

---

## 📊 Exemplo do Gráfico

<div align="center">
  <img src="./graph/grafico_1764167158.png" alt="Gráfico de Decaimento" width="80%" />
</div>

---

## 🧠 Conceito Matemático

O projeto demonstra o uso de **limites aplicados** em:

V(n) = V0(1 - r)^n

Com limite:

lim_{n -> infty} V(n) = 0 \quad \text{para } 0 < r < 1

---

## 🛠 Tecnologias Utilizadas

- 🐍 Python  
- 📐 SymPy (cálculo simbólico)  
- 📊 Matplotlib (gráficos)  
- 🎨 Termcolor (cores no terminal)  
- 🖥 OS + ClearScreen para experiência CLI  

---

## 📦 Instalação

```bash
git clone https://github.com/TheTekig/DecaimentoAtivo-Calculo.git
cd SEU_REPOSITORIO
pip install -r requirements.txt
python main.py

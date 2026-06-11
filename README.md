# Comparador de Figurinhas

Script em Python para comparar listas de **figurinhas repetidas** e **figurinhas faltantes**, identificando automaticamente quais figurinhas uma pessoa possui e que a outra precisa.

## Funcionalidades

* Compara figurinhas repetidas e faltantes.
* Organiza automaticamente os dados por seleção/país.
* Aceita múltiplos formatos de entrada.
* Ignora quantidades de repetição (`1x`, `2x`, `3x`, etc.).
* Exibe apenas as correspondências encontradas.
* Funciona com listas copiadas diretamente de planilhas, grupos de WhatsApp ou anotações manuais.

---

## Como funciona

O programa recebe duas listas:

### Repetidas

Figurinhas que uma pessoa possui para troca.

Exemplo:

```text
BRA: 01(2x), 04(1x), 15(3x)
ARG: 02(1x), 07(2x)
```

### Faltantes

Figurinhas que outra pessoa precisa.

Exemplo:

```text
BRA: 01, 04, 18
ARG: 02, 05
```

Após a comparação, o sistema informa quais figurinhas podem ser trocadas.

Exemplo de saída:

```text
=== FIGURINHAS ACHADAS ===

Total encontrado: 3

BRA: 01, 04
ARG: 02
```

---

## Formatos Aceitos

O parser foi desenvolvido para aceitar diferentes formatos automaticamente.

Todos os exemplos abaixo são válidos:

```text
BRA 04
```

```text
BRA: 04
```

```text
BRA - 04
```

```text
BRA -> 04
```

```text
BRA: 01, 04, 15, 18
```

```text
BRA 01 04 15 18
```

```text
BRA | 01 | 04 | 15 | 18
```

```text
BRA: 01(2x), 04(1x), 15(3x)
```

---

## Requisitos

* Python 3.8 ou superior

Verificar versão:

```bash
python --version
```

---

## Execução

Clone o repositório:

```bash
git clone https://github.com/RondonGVM/ComparadorFigurinhas.git
```

Entre na pasta:

```bash
cd comparador-figurinhas
```

Execute:

```bash
python comparador.py
```

---

## Casos de Uso

* Álbum de Copa do Mundo


---

## Tecnologias

* Python
* Expressões Regulares (Regex)

---

## Licença

Este projeto é livre para uso pessoal e educacional.

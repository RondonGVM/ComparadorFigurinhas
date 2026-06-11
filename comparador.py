import re

ORDEM_PAISES = [
    "FWC", "CC", "MEX","RSA", "KOR", "CZE", "CAN", "BIH", "QAT",
    "SUI", "BRA", "MAR", "HAI", "SCO", "USA", "PAR", "AUS",
    "TUR", "GER", "CUW", "CIV", "ECU", "NED", "JPN", "SWE",
    "TUN", "BEL", "EGY", "IRN", "NZL", "ESP", "CPV", "KSA",
    "URU", "FRA", "SEN", "IRQ", "NOR", "ARG", "ALG", "AUT",
    "JOR", "POR", "COD", "UZB", "COL", "ENG", "CRO", "GHA",
    "PAN"
]

# ==========================================
# REPETIDAS (Pessoa 1)
# ==========================================

repetidas_texto = """
COLE AQUI AS FIGURINHAS REPETIDAS
"""

# ==========================================
# FALTANTES (Pessoa 2)
# ==========================================

faltantes_texto = """
COLE AQUI AS FIGURINHAS FALTANTES
"""

def parse_universal(texto):
    resultado = {}

    for linha in texto.strip().splitlines():
        linha = linha.strip().upper()

        if not linha:
            continue

        match_pais = re.match(r'^([A-Z]{3})', linha)

        if not match_pais:
            continue

        pais = match_pais.group(1)

        resultado.setdefault(pais, set())

        # Captura apenas números de figurinhas,
        # ignorando quantidades do tipo (4x)
        numeros = re.findall(r'(?<!\()(?<!\d)(\d{1,2})(?!X\))', linha)

        for n in numeros:
            numero = int(n)

            if 0 <= numero <= 20:
                resultado[pais].add(numero)

    return resultado


def imprimir_lista(titulo, dados):
    print(f"\n=== {titulo} ===\n")

    for pais in ORDEM_PAISES:
        if pais in dados:
            numeros = ", ".join(
                f"{n:02d}" for n in sorted(dados[pais])
            )
            print(f"{pais}: {numeros}")

    extras = sorted(set(dados.keys()) - set(ORDEM_PAISES))

    for pais in extras:
        numeros = ", ".join(
            f"{n:02d}" for n in sorted(dados[pais])
        )
        print(f"{pais}: {numeros}")


def comparar(repetidas, faltantes):
    encontrados = {}

    todos_paises = set(repetidas.keys()) | set(faltantes.keys())

    for pais in todos_paises:
        rep = repetidas.get(pais, set())
        fal = faltantes.get(pais, set())

        intersecao = sorted(rep & fal)

        if intersecao:
            encontrados[pais] = intersecao

    return encontrados



repetidas = parse_universal(repetidas_texto)
faltantes = parse_universal(faltantes_texto)


resultado = comparar(repetidas, faltantes)

print("\n=== FIGURINHAS ACHADAS ===\n")

if resultado:
    total = sum(len(v) for v in resultado.values())

    print(f"Total encontrado: {total}\n")

    for pais in ORDEM_PAISES:
        if pais in resultado:
            numeros = ", ".join(
                f"{n:02d}" for n in resultado[pais]
            )
            print(f"{pais}: {numeros}")

    extras = sorted(set(resultado.keys()) - set(ORDEM_PAISES))

    for pais in extras:
        numeros = ", ".join(
            f"{n:02d}" for n in resultado[pais]
        )
        print(f"{pais}: {numeros}")

else:
    print("Nenhuma figurinha encontrada.")
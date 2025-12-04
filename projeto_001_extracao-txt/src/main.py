import re
import sys
import csv

# Verifica se o número correto de argumentos foi fornecido
if len(sys.argv) != 3:
    print("Uso correto: utilize 3 argumentos")
    print("Exemplo: python main.py <arquivo_entrada.txt> <arquivo_saida.csv>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Expressão Regular para encontrar valores monetários no formato brasileiro:
# 1. Opcionalmente "R$" ou "RS" (com ou sem espaço).
# 2. Sequência de números com separador de milhar opcional (o ponto '.').
# 3. Opcionalmente, uma vírgula ',' seguida de dois dígitos (para centavos).
# Exemplos que correspondem: R$ 19,90 | 29,00 | 150 | 2.345,67
# REGEX_VALOR = r'(?:R\$?\s?)?(\d{1,3}(?:\.\d{3})*(?:,\d{2})?|\d+(?:,\d{2}))'

# NOVO REGEX: Mais rigoroso. Exige o 'R$' ou a vírgula ',' decimal.
# Ele evita a captura de números inteiros soltos (como 10, 150, 2024).
REGEX_VALOR = r'(?:R\$?\s?)?(\d{1,3}(?:\.\d{3})*(?:,\d{2}))|\d{1,3}(?:\.\d{3})*(?:,\d{2})'

def extrair_e_converter_valores(texto):
    """Extrai valores do texto e os converte para o formato decimal (float)."""
    # Usando findall com o NOVO REGEX
    valores_brutos = re.findall(REGEX_VALOR, texto)
    valores_limpos = []
    
    for valor_tupla in valores_brutos:
        # Pega o primeiro elemento não vazio da tupla (resultado da RegEx)
        valor = valor_tupla[0] if isinstance(valor_tupla, tuple) else valor_tupla

        # 1. Limpeza inicial
        valor_limpo = re.sub(r'R\$?\s?', '', valor).strip()
        # valor_limpo = re.sub(r'R$?\s?', '', valor).strip()
        # valor_limpo = re.sub(r'R\\$?\s?', '', valor).strip()
        # valor_limpo = re.sub(r'R\$\s*', '', valor).strip()
        
        # 2. Troca de separadores: milhar (ponto) por nada; decimal (vírgula) por ponto
        valor_limpo = valor_limpo.replace('.', '')
        valor_final = valor_limpo.replace(',', '.')
        
        try:
            # Tenta converter para float e formata com duas casas
            valores_limpos.append(f"{float(valor_final):.2f}")
        except ValueError:
            # Isso deve capturar '129' (inteiro) se ele não tiver sido pego pela RegEx
            # E se ele for um número válido, formatá-lo.
            try:
                # Tentativa de conversão de inteiro (ex: "129")
                if valor.isdigit():
                    valores_limpos.append(f"{float(valor):.2f}")
                else:
                    continue
            except ValueError:
                continue
            
    return valores_limpos

def main():
    """Função principal: lê o arquivo, extrai os valores e grava no CSV."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada '{input_file}' não encontrado.")
        sys.exit(1)

    valores_extraidos = extrair_e_converter_valores(conteudo)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['valor']) # Cabeçalho do CSV
        for valor in valores_extraidos:
            writer.writerow([valor])
            
    print(f"Sucesso! {len(valores_extraidos)} valores extraídos e salvos em '{output_file}'.")

if __name__ == "__main__":
    main()
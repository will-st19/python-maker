import csv
import argparse
import time
import requests
from requests.exceptions import RequestException

def parse_arguments():
    """Configura os argumentos da linha de comando."""
    parser = argparse.ArgumentParser(description="Validador de URLs em Lote")
    parser.add_argument("input_file", help="Caminho para o arquivo CSV de entrada")
    parser.add_argument("output_file", help="Caminho para o arquivo CSV de saída")
    return parser.parse_args()

def validate_url(url):
    """
    Valida uma única URL e retorna seus dados.
    """
    # Garante que a URL tenha esquema (http/https) para evitar erros do requests
    if not url.startswith(('http://', 'https://')):
        target_url = f"https://{url}" # Tenta HTTPS por padrão
    else:
        target_url = url

    headers = {
        'User-Agent': 'ValidadorURL/1.0 (Projeto 002)'
    }

    start_time = time.time()
    
    try:
        # allow_redirects=False é CRUCIAL para detectar status 301/302
        # timeout=10 evita que o script trave em sites lentos
        response = requests.get(target_url, headers=headers, timeout=10, allow_redirects=False)
        
        status_code = response.status_code
        elapsed_ms = int((time.time() - start_time) * 1000)
        
        # Determina a categoria do status
        if 200 <= status_code < 300:
            status_text = "valida"
        elif 300 <= status_code < 400:
            status_text = "redireciona"
        elif status_code >= 400:
            status_text = "quebrada"
        else:
            status_text = "desconhecido"

    except RequestException:
        # Captura erros de DNS, conexão recusada, timeout, SSL, etc.
        status_code = 0
        status_text = "offline"
        elapsed_ms = 0

    return {
        "url": url,
        "status_code": status_code,
        "status": status_text,
        "tempo_ms": elapsed_ms
    }

def process_csv(input_path, output_path):
    """
    Lê o CSV de entrada, valida as URLs e escreve no CSV de saída.
    """
    try:
        with open(input_path, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            
            # Verifica se a coluna 'url' existe
            if 'url' not in reader.fieldnames:
                print(f"Erro: O arquivo '{input_path}' não possui a coluna 'url'.")
                return

            # Prepara o arquivo de saída
            fieldnames = ['url', 'status_code', 'status', 'tempo_ms']
            
            print(f"--- Iniciando processamento de: {input_path} ---")

            with open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                count = 0
                for row in reader:
                    
                    # --- NOVO BLOCO DE LIMPEZA MAIS ROBUSTO AQUI ---
                    url_with_comment = row['url'].strip()
                    
                    # 1. Ignora tudo após o primeiro caractere '#' (comentários)
                    # 2. Pega apenas a primeira parte [0] e remove espaços em branco extras
                    url_to_check = url_with_comment.split('#')[0].strip() 
                    # --- FIM DO NOVO BLOCO ---
                    
                    if not url_to_check:
                        continue

                    print(f"Verificando: {url_to_check}...", end='\r')
                    
                    result = validate_url(url_to_check)
                    writer.writerow(result)
                    count += 1
            
            # ... (código omitido) ...

    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada '{input_path}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    args = parse_arguments()
    process_csv(args.input_file, args.output_file)
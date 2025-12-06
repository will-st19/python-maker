import sys
import os
from pypdf import PdfWriter

# --- 1. VERIFICAÇÃO INICIAL DE ARGUMENTOS ---
if len(sys.argv) != 3:
    print("🚨 ERRO: Número incorreto de argumentos.")
    print("Uso correto: python merge_pdfs.py <pasta_entrada> <arquivo_saida.pdf>")
    sys.exit(1)

input_folder = sys.argv[1]
output_filename = sys.argv[2]

# --- VALIDAÇÃO DA EXTENSÃO ---
if not output_filename.lower().endswith(".pdf"):
    print("🚨 ERRO: O segundo argumento deve ter a extensão '.pdf'.")
    sys.exit(1)

# --- VERIFICAÇÃO DE NOME VAZIO OU APENAS EXTENSÃO ---
# Checa se o nome base do arquivo está vazio.
name_base, ext = os.path.splitext(output_filename)
if not name_base:
    print("🚨 ERRO: O nome do arquivo PDF não pode ser apenas a extensão (ex: '.pdf').")
    sys.exit(1)

# --- Monta o caminho completo usando a pasta de entrada
full_output_path = os.path.join(input_folder, output_filename)

# --- 2. VERIFICAÇÃO DA PASTA DE ENTRADA ---
try:
    if not os.path.isdir(input_folder):
        raise FileNotFoundError(f"Pasta de entrada não encontrada: '{input_folder}'")
except FileNotFoundError as e:
    print(f"❌ ERRO FATAL: {e}")
    sys.exit(1)

# --- 3. PREPARAÇÃO DA LISTA DE ARQUIVOS ---
try:
    # Lista todos os arquivos na pasta
    arquivos = os.listdir(input_folder)

    # Filtra, ordena e monta o caminho completo
    pdfs = [f for f in arquivos if f.lower().endswith(".pdf")]
    pdfs_ordenados = sorted(pdfs)
    pdfs_completos = [os.path.join(input_folder, f) for f in pdfs_ordenados]

    if not pdfs_completos:
        print(f"⚠️ AVISO: Não foi encontrado nenhum arquivo PDF na pasta '{input_folder}'.")
        sys.exit(0) # Sai sem erro se não houver PDFs

except Exception as e:
    print(f"❌ ERRO: Falha ao processar a pasta '{input_folder}'. Detalhes: {e}")
    sys.exit(1)

# --- 4. PROCESSO DE MERGE ---
merger = PdfWriter()
pdfs_anexados = 0

print(f"\n📂 Iniciando merge de {len(pdfs_completos)} arquivo(s)...")

for pdf_path in pdfs_completos:
    pdf_name = os.path.basename(pdf_path)
    try:
        # Tenta anexar o PDF. O pypdf pode levantar exceções aqui
        merger.append(pdf_path)
        print(f"   ✅ Anexado: {pdf_name}")
        pdfs_anexados += 1
    except Exception as e:
        # Captura o erro (ex: 'Object 0 0 not defined') e registra
        print(f"   🛑 FALHA no arquivo {pdf_name}: O arquivo está corrompido ou malformado. Será IGNORADO. Detalhes: {e}")

# --- 5. ESCRITA DO ARQUIVO FINAL E LIMPEZA ---
try:
    if pdfs_anexados > 0:
        # Use 'with open' para garantir que o arquivo seja fechado corretamente
        with open(full_output_path, "wb") as saida:
            merger.write(saida)
        
        print(f"\n✨ SUCESSO! {pdfs_anexados} arquivo(s) combinado(s) em '{full_output_path}'")
        
        # Avisa se alguns arquivos foram ignorados
        if pdfs_anexados < len(pdfs_completos):
            print(f"⚠️ Nota: {len(pdfs_completos) - pdfs_anexados} arquivo(s) foram ignorados devido a erros de leitura.")

    else:
        print("\n❌ ERRO: Nenhum PDF válido pôde ser anexado. Arquivo de saída não criado.")

except Exception as e:
    print(f"\n❌ ERRO FATAL ao tentar gravar o arquivo de saída '{output_filename}'. Detalhes: {e}")

finally:
    # Garante que o objeto merger seja fechado, liberando recursos
    merger.close()
    print("Processo finalizado.")
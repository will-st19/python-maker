# Projeto 003 — Misturador de PDFs (Merge)

## Problema
No dia a dia de escritórios, RH, contabilidade e até vida pessoal, é comum precisar unir vários PDFs espalhados em uma pasta (relatórios, boletos, laudos, páginas soltas) em um único arquivo final legível.
Fazer isso manualmente é lento e repetitivo.

## Solução
Um script simples em Python que recebe uma pasta com PDFs, 
combina todos em ordem alfabética e gera um único PDF final.
Sem dependências complexas e sem interface gráfica — rápido, direto ao ponto.

## Como usar
python merge_pdfs.py input_folder output.pdf

# Exemplo de entrada
Pasta documentos/ contendo:

1_intro.pdf
2_contrato.pdf
3_anexos.pdf

# Exemplo de saída
final_merged.pdf

## Melhorias futuras
- Ordenação personalizada dos arquivos
- Suporte a escolha manual das páginas
 -Versão GUI com Tkinter para usuários não técnicos
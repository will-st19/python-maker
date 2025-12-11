# Projeto 007 — Análise de Spam SMS (NLP Básico)

## Problema
Mensagens de SMS podem ser classificadas como spam ou ham (legítimas).
Este projeto analisa um dataset de spam para entender padrões que diferenciam os dois tipos de mensagem usando técnicas simples e interpretáveis.

## Solução
O script:
    * carrega o dataset spam.csv;
    * faz limpeza textual básica;
    * cria features simples (tamanho da mensagem, % de maiúsculas, contagem de !, presença de links, número de palavras);
    * compara estatísticas entre spam e ham;
    * executa um teste de hipótese (t-test);
    * gera visualizações (histogramas, boxplot, wordcloud);
    * imprime estatísticas chave para análise rápida.

Serve como introdução a análise textual prática (NLP leve).

## Como usar
python main.py

## Exemplo de entrada
Trecho do CSV:

    v1,v2
    ham,Ok lar... call me once you reach home
    spam,WINNER!! Your code is FREE123. Claim now at http://spam.com
    ham,I'm going to buy milk later

## Exemplo de saída
=== Estatísticas rápidas ===
      msg_len  word_count  caps_perc  num_exclam   has_link
ham     52.31        9.12       0.04        0.11       0.01
spam   138.44       23.54       0.18        1.92       0.67

T-test tamanho da mensagem Ham vs Spam: p-value = 0.0000

=== Concluído com sucesso ===

## Melhorias futuras
- Adicionar modelo simples de classificação (Logistic Regression / Naive Bayes)
- Criar pipeline de pré-processamento usando sklearn
- Exportar gráficos automaticamente para pasta /reports
- Criar notebook .ipynb resumindo a análise para apresentação
- Medir mais features textuais (TF-IDF, bigrams, etc.)
# Projeto 005 — Conversor de Moedas (API Flask)

## Problema
Em tarefas do dia a dia (financeiro, admin, pessoal ou pequenas automações), é comum precisar converter valores entre moedas diferentes.  
Fazer isso manualmente, pesquisando valores toda hora, gera erros e toma tempo.

Mesmo sendo simples, conversores rápidos ajudam em planilhas, scripts e micro-processos internos.

## Solução
Uma API mínima em Flask que recebe um valor (`amount`) e converte entre moedas usando taxas fixas de exemplo.  
Ideal para:
- demonstrações,
- estudos,
- protótipos,
- ou integração em scripts maiores.

A API valida parâmetros, retorna erros claros e responde em JSON.

## Como usar

### 1. Rodar o servidor
python app.py
    API disponível em: http://127.0.0.1:5000/convert

Fazer uma requisição
    Exemplo usando curl:
        curl "http://127.0.0.1:5000/convert?amount=10&from=USD&to=BRL"
        Resposta esperada:
        {
            "amount": 10.0,
            "from_currency": "USD",
            "to_currency": "BRL",
            "converted_amount": "52.50"
        }

    Exemplos de erro
        Parâmetros faltando
            curl "http://127.0.0.1:5000/convert"
            {
                "error": "Missing parameters",
                "parameters_missing": ["amount", "from", "to"]
            }
            
        Valor inválido
            curl "http://127.0.0.1:5000/convert?amount=abc&from=USD&to=BRL"
                {"error": "Invalid amount"}

        Moeda não suportada
            curl "http://127.0.0.1:5000/convert?amount=10&from=JPY&to=USD"
                {"error": "Currency not supported"}

# Melhorias futuras
- Conectar a API a um serviço de câmbio real (ex.: exchangerate.host)
- Adicionar mais moedas
- Suportar envio via POST com body JSON
- Adicionar testes automatizados básicos
- Criar versão com taxas atualizadas diariamente em cache
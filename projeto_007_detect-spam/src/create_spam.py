import os
import pandas as pd
import numpy as np
import random

# ==========================
# Configurações
# ==========================
n_rows = 1000
spam_ratio = 0.15

ham_phrases = [
    "Call me when you get home",
    "Are we still meeting today",
    "Don't forget to send the report",
    "See you tomorrow",
    "Ok thanks",
    "I will check and let you know",
    "The meeting starts at 3 pm",
    "Please confirm receipt",
    "Lunch today?",
    "Let’s talk later"
]

spam_phrases = [
    "Congratulations! You won a prize!!! Click now!",
    "URGENT: Your account has been compromised. Verify immediately",
    "Free entry to win cash. Visit our website now",
    "You have been selected for a reward. Claim here",
    "Limited offer!!! Buy now and save big",
    "Get cheap loans online. No credit check",
    "Your number was chosen for a bonus! Click the link",
    "This is not a scam. Transfer money to unlock funds",
    "CLAIM your free gift card today!!!",
    "Exclusive offer only for you. Act fast!"
]

# ==========================
# Função para gerar mensagem aleatória
# ==========================
def random_message(source_list):
    base = random.choice(source_list)
    # adiciona pequenas variações para não ficar artificial
    noise = [
        "", 
        ".", 
        " please", 
        " now", 
        " thank you", 
        "!!!", 
        " asap"
    ]
    return base + random.choice(noise)

# ==========================
# Gerar dataset
# ==========================
rows = []

for _ in range(n_rows):
    if random.random() < spam_ratio:
        label = "spam"
        msg = random_message(spam_phrases)
    else:
        label = "ham"
        msg = random_message(ham_phrases)

    rows.append([label, msg])

df = pd.DataFrame(rows, columns=["v1", "v2"])

# ==========================
# Salvar arquivo
# ==========================
path_data = os.path.join(os.path.dirname(__file__), "..", "data", "spam.csv")
path_data = os.path.abspath(path_data)
df.to_csv(path_data, index=False, encoding="utf-8")

print("Arquivo spam.csv criado com sucesso!")
print(df.head())

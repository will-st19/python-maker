import pandas as pd
import matplotlib.pyplot as plt
import string
import re
import os
from wordcloud import WordCloud
import numpy as np
from scipy.stats import ttest_ind

# ==========================
# 1. Carregar e preparar dados
# ==========================
path_data = os.path.join(os.path.dirname(__file__), "..", "data", "spam.csv")
path_data = os.path.abspath(path_data)
df = pd.read_csv(path_data, encoding='utf-8')
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# ==========================
# 2. Limpeza simples do texto
# ==========================
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    return text

df["clean"] = df["message"].apply(clean_text)

# ==========================
# 3. Feature Engineering leve
# ==========================
df["msg_len"] = df["message"].apply(len)
df["word_count"] = df["clean"].str.split().apply(len)
df["caps_perc"] = df["message"].apply(lambda x: sum(1 for c in x if c.isupper()) / len(x))
df["num_exclam"] = df["message"].apply(lambda x: x.count("!"))
df["has_link"] = df["message"].apply(lambda x: 1 if "http" in x or "www" in x else 0)

# ==========================
# 4. Estatísticas básicas
# ==========================
ham = df[df["label"] == "ham"]
spam = df[df["label"] == "spam"]

print("\n=== Estatísticas rápidas ===")
print(df.groupby("label")[["msg_len", "word_count", "caps_perc", "num_exclam", "has_link"]].mean())

# Teste de hipótese: spam tem mensagens maiores?
t_stat, p_val = ttest_ind(ham["msg_len"], spam["msg_len"])
print(f"\nT-test tamanho da mensagem Ham vs Spam: p-value = {p_val:.4f}")

# ==========================
# 5. Visualizações
# ==========================

# 5.1 Distribuição de mensagens ham vs spam
plt.figure(figsize=(6,4))
df["label"].value_counts().plot(kind="bar", color=["green", "red"])
plt.title("Quantidade de mensagens (Ham vs Spam)")
plt.xlabel("Label")
plt.ylabel("Contagem")
plt.tight_layout()
plt.show()

# 5.2 Distribuição do tamanho das mensagens
plt.figure(figsize=(8,4))
plt.hist(ham["msg_len"], bins=40, alpha=0.7, label='Ham')
plt.hist(spam["msg_len"], bins=40, alpha=0.7, label='Spam')
plt.title("Distribuição do Tamanho das Mensagens")
plt.xlabel("Tamanho")
plt.ylabel("Frequência")
plt.legend()
plt.tight_layout()
plt.show()

# 5.3 Boxplot comparativo
plt.figure(figsize=(6,4))
df.boxplot(column="msg_len", by="label")
plt.title("Tamanho das Mensagens por Tipo")
plt.suptitle("")
plt.xlabel("Label")
plt.ylabel("Tamanho")
plt.tight_layout()
plt.show()

# 5.4 Wordcloud spam vs ham
spam_text = " ".join(spam["clean"])
ham_text = " ".join(ham["clean"])

wc_spam = WordCloud(width=500, height=300, background_color="white").generate(spam_text)
wc_ham = WordCloud(width=500, height=300, background_color="white").generate(ham_text)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.imshow(wc_spam)
plt.axis("off")
plt.title("Spam WordCloud")

plt.subplot(1,2,2)
plt.imshow(wc_ham)
plt.axis("off")
plt.title("Ham WordCloud")

plt.tight_layout()
plt.show()

print("\n=== Concluído com sucesso ===")

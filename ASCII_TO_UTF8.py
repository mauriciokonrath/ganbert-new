file_path = "/home/mauricio/Downloads/GAN-BERT-main/tokenization.py"

# Ler o conteúdo
with open(file_path, "r", encoding="ascii", errors="ignore") as f:
    content = f.read()

# Adicionar o BOM e salvar como UTF-8
with open(file_path, "w", encoding="utf-8-sig") as f:
    f.write(content)

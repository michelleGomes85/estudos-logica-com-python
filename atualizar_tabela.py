import os

# Caminho para a pasta de exemplos e para o README.md
EXEMPLOS_DIR = "code-atividades"
README_FILE = "README.md"

def atualizar_tabela():
    # Começamos com o cabeçalho da tabela
    tabela = "| Nome do Exemplo           | Link                               |\n"
    tabela += "|---------------------------|------------------------------------|\n"
    
    # Lista todos os arquivos Python na pasta exemplos
    for filename in os.listdir(EXEMPLOS_DIR):
        if filename.endswith(".py"):  # Só vamos pegar os arquivos .py
            # Formatar o nome do exemplo (remover .py e substituir _ por espaço)
            nome = filename.replace('_', ' ').replace('.py', '').title()
            
            # Cria o link para o código
            link = f"./{EXEMPLOS_DIR}/{filename}"
            tabela += f"| {nome:<25} | [Acessar Código]({link}) |\n"
    
    # Lê o conteúdo atual do README.md
    with open(README_FILE, "r", encoding='utf-8') as readme:
        conteudo = readme.readlines()
    
    # Procurar a seção onde a tabela deve começar
    inicio_tabela = -1
    for i, linha in enumerate(conteudo):
        if linha.strip() == "## Exemplos Adicionados":
            inicio_tabela = i + 2  # Linha onde a tabela começa
            break
    
    # Atualiza a tabela no README
    if inicio_tabela != -1:
        # Substitui a parte da tabela existente com a nova
        conteudo = conteudo[:inicio_tabela] + [tabela] + conteudo[inicio_tabela + 1:]
    else:
        # Se não encontrar uma seção, adiciona a seção e a tabela ao final
        conteudo.append("\n## Exemplos Adicionados\n\n" + tabela)
    
    # Salva o conteúdo atualizado de volta no README
    with open(README_FILE, "w", encoding='utf-8') as readme:
        readme.writelines(conteudo)
    
    print("Tabela atualizada com sucesso no README.md!")

if __name__ == "__main__":
    atualizar_tabela()

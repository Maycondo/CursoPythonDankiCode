import os


os.name
print(os.name)

# Verificar se um arquivo existe
print(os.path.exists('modulos'))  # True ou False
print(os.path.exists('associaçao.py'))

# Verificar se m dirtorio existe
print(os.path.exists('Mini_jogo'))
print(os.path.exists('funcoes'))


# Exeplos de caminhos
print(os.path.exists('modulos/outro.py'))

# Criando arquivos
#os.mknod('modulos/olamundo.py')

# Criando um diretorio 
#os.mknod('Teste/')
#os.mknod('')

# Criando um diretorio
# os.mkdir('python')
# Caminho absoluto
#os.mkdir()

# Apagando arquivos

# os.remove('')
os.remove('modulos/olamundo.py')

# Apagando direitos
#os.remove()
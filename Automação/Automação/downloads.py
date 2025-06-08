import os

pasta_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')
arquivos = [os.path.join(pasta_downloads, f) for f in os.listdir(pasta_downloads)]
arquivos = [f for f in arquivos if os.path.isfile(f)]
ultimo_arquivo = max(arquivos, key=os.path.getmtime)
def baixado():
    return ultimo_arquivo

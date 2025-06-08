from PyPDF2 import PdfReader

def verificaNome(arquivo, nome):

    reader = PdfReader(arquivo)
    texto_completo = ""

    for pagina in reader.pages:
        texto = pagina.extract_text()
        if texto:
            texto_completo += texto + "\n"
            
    if nome.lower() in texto_completo.lower():
        return "✅ Seu nome esta no diário oficial de hoje!"
    else:
        return "❌ Seu nome não saiu hoje no diario oficial!"



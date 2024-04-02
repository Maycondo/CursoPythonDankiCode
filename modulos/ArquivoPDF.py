import pydf

pdf = pydf.generate_pdf('<h1>this is html</h1><p>TESTANDO MEU DOCUMENTOS<p>')

with open('Arquivo.pdf', 'wb') as modulos:
    modulos.write(pdf)

import requests, zipfile, io

# Download e descompressão do arquivo zip dos resultados
r = requests.get('http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()



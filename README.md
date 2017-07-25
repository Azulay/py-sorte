# py-sorte
PySorte é uma aplicação Python para análise histórica de jogos da Mega-Sena e sugestão de novas apostas a partir dessas e outras informações.

# Pré-Processamento

1. Criar um objeto para cada Dezena. Ex: dezena_01, dezena_02, ... dezena_60

# Obtenção de Dados

Passo-a-passo básico para se obter os dados para processamento

1. Baixar o arquivo ZIP de sorteios anteriores em http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip

2. Abrir o arquivo ZIP e descompactar o arquivo "D_MEGA.HTM"

# Processamento dos Dados

1. Abrir o arquivo "D_MEGA.HTM" e cadastrar linha a linha como um objeto independente

 - OBS: Estudando agora como fazer isso de forma automatizada com Python e Web Scrapping - Começando por:
	https://pythonhelp.wordpress.com/2013/03/12/acessando-recursos-na-web-com-python/
	https://pythonhelp.wordpress.com/2013/03/18/webscraping-em-python/

2. Trabalhar dados para:

	2.1 Cada Dezena deve ter info sobre qual quadrante ela pertence;
	
	2.2 Cada Dezena deve ter info sobre ser par ou impar;
	
	2.3 Cada Dezena deve ter info sobre ultima vez que saiu;
	
	2.4 Cada Dezena deve ter info sobre quantas vezes saiu;
	
	etc;
	
3. Gerar views de:

	3.1 Números que mais sairam;
	
	3.2 Números que menos sairam;
	
	3.3 Jogos que mais sairam (caso ja tenha havido jogos repetidos);
	
	3.4 Sugestão de jogo no formato Q1-2,Q2-1,Q3-1,Q4-2 com as dezenas mais sorteadas destes quadrantes;
	
	3.5 Sugestão de jogo no formato Q1-2,Q2-1,Q3-1,Q4-2 com as dezenas menos sorteadas destes quadrantes;
	
	etc;

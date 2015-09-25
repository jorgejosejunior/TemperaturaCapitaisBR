__author__ = 'Jorge Jose Junior'
"""
Nesta atualizacao o Usuario digita o nome de uma capital de algum
estado do Brasil e o resultado eh a temperatura.

Primeiro desafio: conseguir instalar o modulo sud no python27
na instalacao nao eh inclusa este modulo quando tentei compilar
o codigo deu erro pedindo o sud ai encontrei na net um comando
para o cmd do windows que baixou e instalou o sud.
Problema resolvido
"""

from suds.client import Client
import xml.dom.minidom
import re
def entradaTemp(tF):
    print '%s F = %s C\n '% (tF, client2.service.FahrenheitToCelsius(tF))
    #print '%s graus em Celsius e = %s Fahrenheit' % (tC, client.service.CelsiusToFahrenheit(tC))

mapaCidades = {}

mapaCidades.update({'ARACAJU':'Aracaju Aeroporto'})
mapaCidades.update({'BELEM':'Belem Aeroporto'})
mapaCidades.update({'BELO HORIZONTE':'Belo Horizonte Aeroporto'})
mapaCidades.update({'CURITIBA':'Curitiba'})
mapaCidades.update({'BRASILIA':'Brasilia Aeroporto'})
mapaCidades.update({'BOA VISTA':'Boa Vista Aeropor-To'})
mapaCidades.update({'CAMPO GRANDE':'Campo Grande Aeroporto'})
mapaCidades.update({'PORTO ALEGRE':'Porto Alegre'})
mapaCidades.update({'CURITIBA':'Curitiba Aeroporto'})
mapaCidades.update({'CUIABA':'Cuiaba Aeroporto'})
mapaCidades.update({'FLORIANOPOLIS':'Florianopolis Aeroporto'})
mapaCidades.update({'FORTALEZA':'Fortaleza Aeropor-To'})
mapaCidades.update({'GOIANIA':'Goiania Aeroporto'})
mapaCidades.update({'JOAO PESSOA':'Joao Pessoa'})
mapaCidades.update({'LONDRINA':'Londrina Aeroporto'})
mapaCidades.update({'MANAUS':'Manaus Aeroporto'})
mapaCidades.update({'MACEIO':'Maceio Aeroporto'})
mapaCidades.update({'MACAPA':'Macapa'})
mapaCidades.update({'NATAL':'Natal Aeroporto'})
mapaCidades.update({'PORTO ALEGRE':'Porto Alegre Aero-Porto'})
mapaCidades.update({'PORTO VELHO':'Porto Velho Aeroporto'})
mapaCidades.update({'RIO BRANCO':'Rio Branco'})
mapaCidades.update({'RECIFE':'Recife Aeroporto'})
mapaCidades.update({'RIO DE JANEIRO':'Rio De Janeiro Aeroporto'})
mapaCidades.update({'SAO LUIS':'Sao Luiz Aeroporto'})
mapaCidades.update({'SAO PAULO':'Sao Paulo Aeropor-To'})
mapaCidades.update({'SALVADOR':'Salvador Aeroporto'})
mapaCidades.update({'TERESINA':'Teresina Aeroporto'})
mapaCidades.update({'VITORIA':'Vitoria Aeroporto'})


pesquisaCidade = raw_input('Digite o nome da capital a ser pesquisada: ')
cidade = pesquisaCidade.upper()
print 'cidade: %s'%cidade

wsdlFile = 'http://www.webservicex.net/globalweather.asmx?WSDL'
#wsdlFile = 'http://www.w3schools.com/webservices/tempconvert.asmx?WSDL'
#serv_url = 'http://www.w3schools.com/webservices/tempconvert.asmx'
client = Client(wsdlFile)
#print client
#Um programa basico seria fazer tres consultas ao site para converter
#tres temperaturas requeridas pelo usuario. Como poderiamos fazer
#isso? Pederiamos utilizar o laco de repeticao for que realizasse
#tres lacos cada um com uma entrada de temperatura diferente.
#print 'Temperatura em Fortaleza = %s '%(client.service.GetCitiesByCountry("Brazil"))
#print client.service.GetWeather("Fortaleza Aeropor-To","Brazil")

#for i in range(0,2):
#    Temperatura = raw_input('Por favor digite a temperatura em Celsius a ser convertida: ')
#    entradaTemp(Temperatura)
#doc.toxml print (client.service.GetWeather("Fortaleza Aeropor-To","Brazil"))
#rXml = client.service.GetWeather("Fortaleza Aeropor-To","Brazil")
#print rXml
with open("este.xml", "w") as arq:
    for chave , endereco in mapaCidades.items():
        if chave == cidade:
            #print cidade , endereco
            arq.write(client.service.GetWeather(endereco,"Brazil"))
            arq.close()

"""
    Aqui esta o fim do acesso ao primeiro webservice
    No primeiro webservice eu coletoo valor da temperatura a
    ser convertido no segundo webservice
"""
arq  = open("este.xml",'r+')
arq.seek(1)
arq.flush()
arq.write("?xml version='1.0'  encoding='utf-8'")
arq.close()

#Acesso ao segundo webservice
DOMTree = xml.dom.minidom.parse("este.xml")
collection = DOMTree.documentElement
print "***********Temperatura em %s WebService 1*********" %cidade
Temperatura =collection.getElementsByTagName('Temperature')[0]
print "Temperatura: %s" % Temperatura.childNodes[0].data
#print Temperatura.childNodes[0].data
ValorFarenheit = Temperatura.childNodes[0].data
TempFarenheit = ValorFarenheit[1:3]
#print TempFarenheit

wsdlFile2 = 'http://www.w3schools.com/webservices/tempconvert.asmx?WSDL'
client2 = Client(wsdlFile2)
print '*******Temperatura Convertida no WebService 2***********'
entradaTemp(str(TempFarenheit))

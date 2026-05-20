#Gabrielle Guarani da Silva e Luiza Hackenhaar Naziazeno

from flask import Flask
from flask import jsonify #add o import jsonify
import requests #instalacao do requests



app = Flask(__name__)

dados_dados = [] #para fazer o delete

def carregar_dados():
    #requests sem o s
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()

    return [
        {
            "id": item["id"],
            "nome": item["name"],
            "email": item["email"]
        }
        for item in data
    ]

dados = carregar_dados()

#Listagem está faltando o ,methods=['GET'] para listar os dados e usar o jsonify para retornar um json
@app.route('/dados',methods=['GET'])
def listar():
    return jsonify(dados)

#Está faltando o ,methods=['GET']
@app.route('/dados/<int:id>',methods=['GET'])
def buscar(id):
    for item in dados:
        if item["id"] == id:
            return jsonify(item)

#faltando o jsonify e add o erro 404
    return jsonify({"erro": "não encontrado"} ),404

@app.route('/dados', methods=['POST'])
def adicionar():
    novo = requests.get_json()

    #removido o dados.append daqui para fazer igual aos slides
    novos_dados = {
        "id": len(dados) + 1, #faltando o +1 pra criar um novo dado
        "nome": novo["nome"],
        "email": novo["email"]
    }
    
    #add o append aqui conforme os slides
    dados.append(novos_dados) 
    return jsonify(novos_dados),201 #add o jsonify ao return e o erro 201

#Bonus: delete
@app.route('/dados/<int:id>', methods = ['DELETE'])
def deletar_dados(id):
    dado_encontrado = None

    for dados in dados_dados:
      if dados["id"] == id:
       dado_encontrado = dados
       break 
   
    if dado_encontrado:
       dados_dados.remove(dado_encontrado)
       return jsonify({"mensagem" : "Dado deletado com sucesso"})
   
    return jsonify({"erro": "Dado não encontrado" }),404

#__name__ definido errado,faltando 1_ no inicio e no fim
# e add _ ao main no inicio e no fim
if __name__ == '__main__':
    app.run(debug=True)

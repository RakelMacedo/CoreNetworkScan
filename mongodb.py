from pymongo import MongoClient


# Função que insere os dados no MongoDB
def Insert_MongoDB(data, collection):

    try:
        # Tenta criar uma conexão com o servidor MongoDB local
        client = MongoClient("mongodb://localhost:27017/")

        # Acessa o banco de dados "port_scans"
        db = client["CoreNetwork"]

        # Acessa a coleção "scan_results" dentro do banco de dados
        collection = db[collection]

        # Insere os dados no MongoDB
        collection.insert_one(data)

        # Fecha a conexão com o MongoDB
        client.close()

        print("\n[+] Resultados do scan inseridos no MongoDB com sucesso!\n")

    except Exception as e:
        print(f"\n[-] Ocorreu um erro ao inserir os resultados no MongoDB, veja abaixo:\n{e}")
        print("\n[-] Certifique-se de que você possui o MongoDB instalado e em execução.\n")


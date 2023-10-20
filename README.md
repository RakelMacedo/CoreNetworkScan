# CoreNetworkScan
Software desenvolvido para escanear pacotes em transito localmente dos protocolos TCP e Ethernet. O scan terá integração com o MongoDB e API criada com o Flask.

![network_](https://github.com/RakelMacedo/CoreNetworkScan/assets/78339857/6f0ef9ba-4434-42ab-9ab7-c7f9c601ba4e)

# Badges
![badge1](https://img.shields.io/badge/python-3.11-blue) ![badge2](https://img.shields.io/badge/status-aguardando%20revis%C3%A3o-yellow) ![badge3](https://img.shields.io/badge/testado%20por-GrupoDosCrias-green)

# Índice 
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Vídeo Explicativo](#vídeo-explicativo)
* [Status do Projeto](#status-do-projeto) 
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Link de vídeo explicativo](TBD)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras-do-projeto)
* [Licença](#licença)
* [Conclusão](#conclusão)

# Descrição do Projeto

O presente projeto tem como objetivo realizar a interceptação de dados na rede e armazenar os PDUs (Packet Data Unit) como objetos JSON no MongoDB, sendo todas as ações feitas através de um API utilizando os métodos HTTP implementados no Python/Flask. Para a composição da aplicação foram escolhidos dois protocolos para interceptar os dados.

# Vídeo Explicativo

* [TBD]

# Status do Projeto

O projeto foi desenvolvido mediante a proposta de trabalho do professor Fábio Cabrini, na disciplina "Coding for Security", como sexto "checkpoint" para a turma 1TDCG da Faculdade de Administração e Informática Paulista. Aguardando revisão e aprovação pelo docente responsável. 

# Funcionalidades e Demonstração da aplicação

## Funcionamento dos algoritmos

Este código Python consiste em duas funções, Ethernet e TCP, que permitem a captura e análise de pacotes de rede Ethernet e pacotes TCP. A função Ethernet analisa pacotes Ethernet, extraindo informações como endereços MAC de origem e destino, bem como o tipo Ethernet. Quando encontra um pacote TCP, extrai informações detalhadas, como portas de origem e destino, números de sequência e flags TCP.

Ambas as funções utilizam sockets brutos para captura de pacotes em um nível mais baixo. O programa pode ser interrompido pelo usuário com uma exceção KeyboardInterrupt, e, ao final, fecha o socket bruto. As duas funções são chamadas sequencialmente no código, permitindo a captura contínua de pacotes Ethernet e pacotes TCP.

## Execução

* Primeiro, abra um terminal no seu sistema Linux.

* Clone o repositório no diretório desejado diretamente pelo terminal Linux/MacOS, com o comando:
```
git clone https://github.com/RakelMacedo/CoreNetworkScan.git
```
* Em seguida, utilizando o terminal, vá para o diretório onde foi baixado o repositório:
```
cd CoreNetworkScan
```
* Instale as dependencias:
```
pip install -r requirements.txt
```
* Execute o seguinte comando para iniciar a API:
```
sudo python3 api.py
```
* Deixe o código em execução para a API ficar ativa e capturar e processar pacotes.

* Abra o http://127.0.0.1 ou http://localhost para ver a página inicial.
![bemvindo](https://github.com/RakelMacedo/CoreNetworkScan/assets/78339857/efca51f0-7082-4fc6-a8bb-104c72d88778)

* Antes de iniciar a aplicação, verifique se você já tem o MongoDB instalado no seu sistema. Caso não o tenha, siga as instruções de instalação do MongoDB apropriadas para o seu sistema operacional. Se você já possui o MongoDB instalado, inicie o serviço do MongoDB com os seguintes passos:

* Abra um terminal no seu sistema Linux. Certifique-se de estar logado como superusuário (root) ou tenha permissões de superusuário.

* Execute o seguinte comando para iniciar o serviço do MongoDB:
```
systemctl start mongod
```
Agora, a API está em execução peonta para rodar e vizualizar dados dos protocolos TCP e Ethernet e o MongoDB está pronto para ser utilizado. 

# Link de vídeo explicativo

# Pessoas Desenvolvedoras do Projeto

Carolina Camacho

João Victor Santos Alves

Rakel de Macedo Oliveira

# Licença

 General Public License

# Conclusão

A implementação das funções de captura e análise de pacotes de rede nos permite obter uma visão detalhada do tráfego de dados em uma rede local, possibilitando ajustes personalizados e otimizações. Da mesma forma que nas funções de ordenação, o conhecimento interno da aplicação nos permite adaptá-la às necessidades específicas, explorar novas análises de tráfego e integrá-la a sistemas de segurança. A capacidade de ajuste fino baseada em diferentes cálculos matemáticos torna a aplicação flexível e pronta para enfrentar desafios em constante evolução no gerenciamento de redes e segurança cibernética.

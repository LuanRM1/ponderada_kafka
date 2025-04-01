# Integração MQTT com Kafka

[Vídeo de demonstração](https://drive.google.com/file/d/1PK1GxNmVjBqfzHkfC57uYfh87VZFD1GS/view?usp=sharing)

Este repositório implementa uma integração entre um broker MQTT (HiveMQ Cloud) e um cluster Kafka rodando em uma VPS. A comunicação entre os dois é feita por um script Python que assina um tópico no HiveMQ e envia os dados recebidos para o Kafka.

## Requisitos

- Python 3.8 ou superior
- Docker e Docker Compose instalados na VPS
- Conta gratuita no HiveMQ Cloud

## Estrutura

O repositório contém:

- `mqtt_to_kafka.py`: script que recebe mensagens MQTT e publica no Kafka
- `docker-compose.yml`: define os containers do Kafka e Zookeeper
- `.env`: arquivo com variáveis de configuração

## Instalação

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Instale as dependências do Python:

```
pip install paho-mqtt kafka-python python-dotenv
```

## Subir o Kafka na VPS

Execute o Docker Compose:

```
docker-compose up -d
```

Crie o tópico no Kafka (na VPS):

```
docker exec kafka kafka-topics.sh --create --topic sensores --bootstrap-server localhost:9092
```

## Executar o sistema

No seu computador local, execute:

```
python3 mqtt_to_kafka.py
```

O script irá conectar ao HiveMQ, escutar o tópico definido no `.env` e enviar qualquer mensagem recebida ao Kafka.

## Testar a publicação MQTT

Acesse o painel do HiveMQ Cloud, vá ao Web Client e publique uma mensagem no tópico:

- Tópico: sensores/temp
- Payload: {"temperatura": 24.8}

## Verificar no Kafka

Na VPS, rode:

```
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sensores --from-beginning
```

# Trabalho em Dupla - Fundamentos de Programação Paralela e Distribuída (FPPD)

## Passos para Configuração e Execução do Projeto

### Passo 1: Preparar o Ambiente

- Coloque os arquivos `docker-compose.yml` e `word_count.py` no mesmo diretório.

### Passo 2: Inicializar os Containers

- Com o terminal aberto no diretório que contém os arquivos, execute o seguinte comando:
  ```bash
  docker-compose up -d

### Passo 3: Executar o Programa

- Após os containers estarem em funcionamento, execute o comando abaixo para iniciar o programa:
    ```bash
    docker exec -it fppd-spark-master-1 spark-submit --master spark://spark-master:7077 /opt/spark-apps/word_count.py

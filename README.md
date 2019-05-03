# artesanato_brasileiro
Aplicação Django/Python para ajudar o Programa do Artesanato Brasileiro a atingir seus objetivos


# Procedimentos para instalar e rodar a aplicação

A seguir tem-se os passos para rodar a aplicação

## Clone do Repositório

A primeira etapa é clonar o projeto para a máquina.

```
git clone https://github.com/edisonik/artesanato_brasileiro.git
```

## Mudar para o diretório clonado

Em seguida deve-se mudar para o diretorio de trabalho.

```
cd artesanato_brasileiro
```

## Criar uma virtualenv para o projeto

Deve-se criar uma virtualevn para ser o ambiente do projeto.

Se não tiver o virtualenv instalado deve rodar os seguintes comandos:

```
sudo apt-get update
sudo apt-get install virtualenv
```

Com o virtualenv já instalado agora basta criar a env:

```
virtualenv  –p  /usr/bin/python3 semantic
```

Para ativar a virtualenv é preciso rodar o seguinte comando. Note que sempre que for exetucar o projeto ou docificar, deve-se rodar esse comando para mudar para o ambiente de desenvolvimento.

```
source semantic/bin/activate
```

## Instalar o requirements

Para instalar os requirements vamos rodar o seguinte comando:

```
pip install requirements.txt
```

Observe que sempre que os requisitos do sistema forem atualizado o arquivo do requirements.txt deve ser atualizado.

## Rodar o projeto

Com o docker e o docker-compose já instalado, para subir a aplicação no container basta rodar o seguinte comando:

```
docker-compose up --biuld -d
```
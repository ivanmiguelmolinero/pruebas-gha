# Documentación Vermont

## Índice

 * [Docker](#Docker)
  * [Kafka y Docker desde cero.](#configurar-kafka-y-docker-desde-cero)
 * [Kafka](#Kafka)

## Docker

Para usar Docker debes decargar Docker Desktop de este [enlace](https://www.docker.com/products/docker-desktop). Una vez hecho esto, puedes descargarte el contenedor de este [repositorio](https://hub.docker.com/r/ivanmiguelmolinero/bitnami-kafka/tags) de Dockerhub con todo lo necesario para usar Kafka o bien puedes descargar [bitnami/kafka](https://hub.docker.com/r/bitnami/kafka/tags) e instalarlo y configurarlo tú todo desde cero para aprender mejor a usar Docker y Kakfa. Nota: en ambos casos debes descargar [Zookeeper](https://hub.docker.com/r/bitnami/zookeeper/tags) para que Kafka funcione.

En caso de querer tener todo configurado desde el principio es recomendable dirigirse a este [repositorio]() y descargar el archivo _docker-compose.yml_ que hay en él. Una vez hecho esto, debes ejecutar el comando `docker-compose -f docker-compose.yml up -d` en una consola de comandos y tendrás todo listo para empezar a usar Kafka.

### Configurar Kafka y Docker desde cero.

Para configura todo desde cero debes descargar Kafka y Zookeeper como se ha dicho previamente (aconsejable usar _dockerfile_ que aparece en este [enlace]()). Con el comando `docker exec -u root -it [nombre_imagen_kafka] /bin/sh` donde "nombre_imagen_kafka" es el nombre que tenga tu imagen de Kafka, nos metemos en la shell del contenedor. Para poder empezar a usarlo debemos instalar varios paquetes previamente:

 * Con el comando `apt update` actualizamos la lista de paquetes que podemos instalar.
 * Con el comando `apt install python3-pip` instalamos _Python3_ y _pip_ necesarios para poder ejecutar el programa "Kafka_json.py" e instalar paquetes adicionales respectivamente.
 * Con el comando `apt install vim` instalamos _Vim_ necesario para poder modificar los archivos de texto.
 * Con el comando `pip3 install kafka-python` isntalamos el módulo _Kafka_ necesario para que el programa funcione.

## Kafka

Apache Kafka es una plataforma de transmisión de eventos distribuidos de código abierto utilizada por miles de empresas para canalizaciones de datos de alto rendimiento, análisis de transmisión e integración de datos. Se basa principalmente en dos programas:

 * **Kafka Consumer**: 

Kafka Consumer se conecta al servidor para recoger (consumir) datos del _topic_ seleccionado. Las particiones de los _topics_ está dividida a través de los consumidores del grupo. Cuando nuevos consumidores llegan al grupo y otros se van, estas particiones son reasignadas en lo que se conoce como _rebalanceo_ del grupo.

 * **Kafka Producer**:

Kafka Producer es conceptualmente mucho más simple que el _consumer_ ya que no necesita grupo de coordinación. El productor mapea cada mensaje de una partición del topic y envía una petición al líder de esa partición.
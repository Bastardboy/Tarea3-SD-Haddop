
<br />
<div align="center">

  <h3 align="center">Sistemas Distribuidos: Tarea 03</h3>

  <p align="center">
    Bastián Castro, David Pazán
  </p>
</div>


## Acerca del proyecto

El objetivo de esta tarea consiste en poner en práctica los conceptos de motor de búsqueda. Para ello se debe hacer uso de tecnlogías que permitan la solución a esta problemática


### 🛠 Construído con:

Esta sección muestra las tecnologías con las que fue construído el proyecto.

* [Hadoop](https://hadoop.apache.org)
* [Python](https://www.python.org)
* [Docker](https://www.docker.com)


## 🔰 Comenzando

Para iniciar el proyecto, primero hay que copiar el repositorio y luego escribir el siguiente comando en la consola:
* docker
```sh
docker build -t hadoop .
```
Para que los contenedores se inician en el ambiente local se utiliza el siguiente comando en la consola:
* docker
```sh
docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
```
### Pre-Requisitos

Tener Docker instalado
* [Installation Guide](https://docs.docker.com/engine/install/debian/)



## 🤝 Uso

### Entrar al contenedor de hadoop
```sh
docker exec -it hadoop bash
```

### Pasos previos a ejecutar el código
Primero se deben crear carpetas propias en el Hadoop con los siguientes comandos
```sh
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input	
```
Al realizar esto, procedemos a darle permisos a *hduser*

```sh
sudo chown -R hduser .
```

A continuación se le pasan los archivos que se obtuvieron de wikipedia, primero moviendonos a la carpeta examples:
```sh
cd examples/
hdfs dfs -put 1/.txt input
hdfs dfs -put 2/.txt input
```

Podemos comprobar que los archivos este subidos con el siguiente comando:
```sh
hdfs dfs -ls input
```
### Ejecución del código MapperReduce
Ahora que tenemos los archivos, procedemos a ejecutar la utilidad de *mapreduce streaming*.
```sh
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/.txt -output /user/hduser/output -mapper ./mapper.py -reducer ./reducer.py
```

Por último, hemos de copiar el output del contenedor en nuestro sistema:
```sh
docker cp output.txt hadoop:/home/hduser/examples
```

### Ejecutar el buscador
Una vez con el output.txt, nos movemos a la carpeta examples que está en el repositorio y ejecutamos el script *convert*
```sh
cd examples/
python3 convert.py
```
Con esto se pasa de un archivo txt a uno JSON que hemos usado como base de datos, sobre el cual se ha de realizar la búsqueda, y para esto es necesario los siguientes pasos

```sh
cd ..
cd seeker/
docker build -t test .
docker run test
```

De esta forma, creamos la imagen del buscador y la corremos, por defecto para realizar la búsqueda se realiza en <a href="http://172.17.0.2:5000/search?search=" target="_blank">http://172.17.0.2:5000/search?search=</a>.

Para efectuar una búsqueda basta con ingresar una palabra delante del símbolo de igual. Dichas palabras se encuentran en lengua inglesa.

## 📹 Video Demostrativo
[![Alt text](https://i.imgur.com/OVbIpJ7.jpg)](https://youtu.be/6NC_x1rzQJw)

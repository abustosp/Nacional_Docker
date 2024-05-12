FROM ubuntu:latest

WORKDIR /server

# RUN add-apt-repository ppa:webupd8team/java -y
RUN apt update -y
# RUN apt-get install oracle-java7-installer -y
# RUN apt install openjdk-17-jdk -y
RUN apt install openjdk-8-jdk -y

COPY client /client
COPY server /server

# Hacer que el contenedor corra nacional_server.jar con los parámetros de memoria especificados
CMD ["java", "-Xms128M", "-Xmx256M", "-XX:PermSize=128M", "-XX:MaxPermSize=256M", "-jar", "nacional_server.jar"]
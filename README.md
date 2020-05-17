# Knight-Proyect-

[![Build Status](https://travis-ci.com/MoisesTapia/Knight-Proyect-.svg?branch=master)](https://travis-ci.com/MoisesTapia/Knight-Proyect-)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/download/releases/3.0/)
[![System](https://img.shields.io/badge/KaliLinux-2020.1-orange)](https://www.kali.org/)
[![Channel](https://img.shields.io/badge/channel-YouTube-red)](https://www.youtube.com/channel/UCiuZK5geN3OCGeBxuXMfHEQ)

#### Depedencias
Para saber las dependencias que ocupamos en el script podemos correr la carpeta __Verify__ que se encuentra en nuestro proyecto, para correr esta carpeta nesecitamos tener instalada la herramienta de [inspec](https://www.inspec.io/downloads/) la cual nos permitira __verificar__ si los modulos que esta herramienta ocupa estan instalados.

#### Instalando Inspec:
Para instalar la herramienta de inspec podemos correr el script de installacion de la siguiente manera:

```bash
$ sudo bash install.sh
```
o
```bash
$ sudo chmod  700 install.sh
$ ./install.sh
```
### Verificar instalacion.

```bash
╭─moisestapia@Equinockx ~/Proyect/Knight-Proyect- ‹master*› 
╰─$ inspec --version
```
#### Forma de ejecutar:

```bash
$ inspec exec Verify/
```
### Aceptar la Licencia de inspec para la aejecucion.
![alt text][logo]

[logo]: https://github.com/dart-security/Knight-Proyect-/blob/master/img/licenses2.png "Inspec"

### Salida de inspec.

![alt text][logo1]

[logo1]: https://github.com/MoisesTapia/Knight-Proyect-/blob/master/img/inspecexec.png "Inspec output"
### Forma de Ejecutar el Script

```bash
$ python3 knightwebpy3.py
```

## Direcciones IP

Si la direccion IP privada no sale en el reposrte del script probablemente es por que no este agregada de manera correcta revisa el codigo en la parte de :

```python
ip_priv = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

```
donde puedes cambiar el __eth0__ por tu interfaz de red que tengas activa en ese momento si tienes una __wlan0__ o __wlan1__ solo agregala entre las comillas para que las puedas visualizar de manera correcta

Ejemplo:
Debian 10:
```python
ip_priv = ni.ifaddresses('enps3')[ni.AF_INET][0]['addr']

```
Kali linux:
```python
ip_priv = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
```
o si tienes __eth1__
```python
ip_priv = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
```

# Demo.
[![asciicast](https://asciinema.org/a/330663.svg)](https://asciinema.org/a/330663)

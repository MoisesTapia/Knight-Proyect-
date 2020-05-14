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

[logo]: https://github.com/dart-security/Knight-Proyect-/blob/master/img/licenses2.png "Inspec output"

### Salida de inspec.

![alt text][logo]

[logo]: https://github.com/dart-security/Knight-Proyect-/blob/master/img/scanninspec.png "Inspec output"
### Forma de Ejecutar el Script

```bash
$ python3 main.py
```


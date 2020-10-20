# Automatizacion

_Prueba de automatizacion_


### Pre-requisitos

_instalar lo necesario segun el archivo requirements.txt_

```
pip install -r requirements.txt
```

## Ejecutando las pruebas 

_Los Tests se encuentran en la carpeta QAT_Example\features_

### Ejecucion desde cmd 

_Nos posicionamos en la carpeta "QAT_Example" y ejecutamos la siguiente linea_

```
Ejemplo: python -m behave QAT_Example\Login.feature
```

### ejecucion desde Pycharm 

_Es necesario configurar pycharm segun la imagen Config_Run.png_

### Ejecucion con Allure 

_Para Realizar reportes con allure es necesario agregar la carpeta que contiene el "allure.bat"
 (allure-commandline-2.10.0\allure-2.10.0\bin) en el path del sistema_
 
_Nos posicionamos en la carpeta "QAT_Example" y ejecutamos la siguiente linea_

```
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features\Login.feature
```
_Lo anterior genero en "allure/results" un json que vamos a usar para hacer el reporte en la carpeta "allure/reports"_

```
allure generate allure/results/ -o allure/reports
```

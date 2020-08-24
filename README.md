# SGC_satreps1.0
Es una página web creada para visualizar los eventos del proyecto SATREPS. Su desarrollo se hizo en python con los siguientes frameworks: Dash y Flask.
## 1. Instalación 
**(Tenga en cuenta que debe tener la carpeta /mnt/escenarios montada.)**

<!---**SI ESTA EN analistas@10.100.100.11 NO ES NECESARIO HACER LA INSTALACIÓN. Pase a 2. Activación**. -->

<!---## Usando Anaconda 
```bash
conda env create -f venv_satreps.yml
conda activate venv_satreps
```-->

### Usando virtualenv
```bash
conda deactivate #En caso de que haya un ambiente de anaconda activo
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Activación 
<!---
## Usando Anaconda
```bash
conda activate venv_satreps
```-->

## Usando virtualenv
** Dentro del repositorio SGC_satreps1.0 **
```bash
conda deactivate #En caso de que haya un ambiente de anaconda activo
source .venv/bin/activate
```

# 3. Demo
Se corre en el servidor 11 de analistas en el puerto 8050.

~~~bash
source .venv/bin/activate
python run.py
~~~
WEB:   http://10.100.100.11:8050
![index -> http://10.100.100.11:8050](images/stp_index.png)

Al hacer click en **Go to SATREPS** los redirige al /home correspondiente al 
visualizador de eventos del proyecto SATREPS: 

WEB:   http://10.100.100.11:8050/home

En la parte izquierda se puede escoger la magnitud y profundidad deseada, luego de ello, el 
mapa interactivo se actualiza con los sismos que cumplen los anteriores parámetros. 

![home -> http://10.100.100.11:8050/home](images/stp_home.png)

En este punto se debe hacer click en el evento que desea observar la simulación. En la parte inferior
izquierda se observa un recuadro titulado como **Website**. En dicho recuadro aparece el enlace que va a redirigir a la página de simulación. 

![home & link -> http://10.100.100.11:8050/home](images/stp_link)
En la anterior figura se hizo click en un sismo ubicado en lat:2.87969, lon:77.76020 con magnitudde M8.5 y profundidad de 50km. Su respectivo enlace se actualizo en el recuadro y corresponde a la siguiente ruta: /mnt/escenarios/21192022202020_2.87969_77.76020_M8.5_50km/html/21192022202020

Al hacer click en el enlace se observa la siguiente simulación:

![escenario -> http://10.100.100.11:8050/home/escenario](images/stp_escenario.png)

**NOTA: No se visualiza la animación mp4 porque se deben actualizar los permisos de ejecución de /mnt/escenarios**

Por último, si se da click en 'source model SWIFT 1' o 'source model SWIFT 2' se pueden ver los modelos generados por swift1 o swift2 respectivamente.

![stp_swift1model -> http://10.100.100.11:8050/home/escenario/21192022202020_src1.html](images/stp_swift1model.png)
![stp_swift2model -> http://10.100.100.11:8050/home/escenario/21192022202020_src2.html](images/stp_swift2model.png)

## 4. Autores

- Emmanuel Castillo ecastillo@sgc.gov.co
- Angel agudelo adagudelo@sgc.gov.co
24-08-2020
# PROYECTO 2 CYK
## Video Demostracion

[Link al video](https://www.youtube.com/watch?v=mRVqUOJNolk)

## Instrucciones
El codigo generado funciona con python. 

- Procura tener instalado python
- Ve al directorio en Proyecto2
```  
cd Proyecto
```
- Instala las dependencias
```  
pip install -r requirements.txt
```

- Dirigete a la carpeta fronted
```  
cd fronted
```
- Corre el programa con
```  
  streamlit run main.py
```
- Esto abrira una pestaña del navegador. Abrela en la direccion siguiente:
```  
  http://localhost:8501
```
- Si quieres colocar tu propio CFG ve a Proyecto2\Files\file.txt y cambia el contenido del archivo
- Recuerda el simbolo epsilon es:
```  
ε
```
- El simbolo de la flecha es:
```  
→
```

## Como usar el programa ?
- Recuerda que debes de tener tu gramatica en Files\files.txt, luego de eso ingresa en el input la cadena w que quieres ver si pertenece al lenguaje y presiona el boton
<img src="Proyecto2\Imagenes\primera.png"  style="object-fit: contain; width: 1000px height: 312px;"/>

- Esto te generara la gramatica normalizada, el parse tree y por ultimo te indica si pertenece o no a la gramatica
<img src="Proyecto2\Imagenes\segunda.png"  style="object-fit: contain; width: 1000px height: 312px;"/>
<img src="Proyecto2\Imagenes\tercera.png"  style="object-fit: contain; width: 1000px height: 312px;"/>
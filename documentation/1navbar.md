# Parte I: Navbar

## Configuraciones generales: 
1. Utilizar etiqueta header para englobar el navbar con una clase "topheader".
2. Utilizar un segundo englobe con la etiqueta nav con una clase "topnav".
3. Para el logo: crear un enlace (&lt;a&gt;) con la clase logo dentro de este enlace van a ir 1° la imagen con height de 50 y width de 50 y 2° un div con el titulo del sitio.
4. Afuera del enlace se crea el menu con etiqueta <ul> y clase "menu" para crear los <li> li*4>a
5. shift + alt + 🠕🠗 → duplica y alt + 🠕🠗 → arrastra
6. Utilizar la libreria normalize (Hace que el sitio se vea igual en cualquier navegador)
7. Para agregar una fuente: 
    1. Ir a google font: el facilitador escoge Montserrat con los estilos Regular 400, Medium 500 y Bold 700
    2. Copiar el link correspondiente y pegar en visualStudio después de la etiqueta title.
8. Resetear los enlaces a none y agregar color
9. :root es un selector generico es igual a utilizar html en css.
## Creando la barra de navegación: 
1. en navbar.css a la clase topnav aplicar display: flex (df) con justify-content: 
space-between (jc). Aplicar un padding de 10px para que los elementos "tenga aire" con respecto a la ventana (espacio)
### Para el logo: 
2. para que la imagen y el nombre de la pagina esten en horizontal aplicar display:flex y align-items: center;
3. aplicar otros estilos como font-size, font-weight y color
4. Para redondear la imagen: .logo img {border-radius:50%}
### Para el menu:
1. Utilizar la clase menu y aplicar los estilos: display: flex, list-style: none (para quitar el punto), resetear el margin y el padding a cero, 
2. aplicar a la etiqueta li: padding: 0;
3. aplicar a la etiqueta a: color, font-size, font-weight, line-height (una forma de central el texto de forma horizontal)
### Para agregar una sombra a la barra:
1. a la clase topheader agregar el estilo box-shadow  0 4px 5 px #xxx (ejeX, ejeY, blur, color)
### Para evitar un ancho maximo:
1. Para lograr un tope: en la clase .topnav agregar el estilo max-width de 980px
2. Y para que este centrado con respecto al header: margin 0 auto; (margin: ⮁ ⇄)
### Para fijar la barra (navbar): 
1. A la clase topheader se debe aplicar los estilos: position: fixed;("que se quede fijado la posición del header con respecto al viewport... viewport es todo lo que vemos en nuestra pagina web")para evitar complicaciones: left: 0; top: 0; (ya que si se le aplica un margin  al contenido se va ir para la 💩  )
2. Aplicar un color al navbar.
3. Para recuperar el ancho de la barra: width: 100%
## Diseño para dispositivos mobiles: (26:50)
1. Agregar las imagenes de "hamburguesa" y "cerrar" dentro etiquetas de botones con las clases "open-menu", "close-menu" y arias-labels "Abrir menú", "Cerrar menu". respectivamente.
2. El boton de hamburguesa debe estar afuera de la lista &lt;ul&gt; y el boton de cerrar debe estar adentro de la lista &lt;ul&gt;

Las imagenes se obtuvieron:
* https://icons8.com/icons/set/close-menu
* https://icons8.com/icons/set/hamburger-button
* https://www.w3schools.com/howto/howto_css_icon_buttons.asp#gsc.tab=0&gsc.q=icon%20close%20svg
* De la Torre (udemy) utiliza: https://tablericons.com/
2. En dispositivos de escritorio estos botones no se tiene que ver: agregar la propiedad css display: none. (29:09)
3. @media (max-width:950px){
    body{
        background-color: blue;
    }
}
Para dispositivos con un ancho menor de 950px se aplica background-color: blue. Aquí se reescribe los estilos.
4. Por defecto el flex-direction es fila por lo tanto se debe aplicar flex-direction: column a la clase .menu;
5. En dispositivos moviles la navegación debe estar fijado con respecto al viewport: aplicar a la clase .menu{ position: fixed; left:0; top: 0; y width: 100%}
6. Para alinear (centrar) como el flex-direction esta en columna la forma en que se procede es en el eje transversal.
7. Cambiar el bc
8. Y para cambiar el color del texto del los items del navbar se debe hacer directamente a los enlaces, cambiar el line-height a 60px.
9. No es necesario que los items tenga padding por eso aplicar padding de cero a la clase .menu li{...}
10. Para que el menu agarre todo el alto del dispositivo es necesario aplicar un height: 100%, a la clase .menu.
11. Para poner una barra automatica para hacer scroll esto cuando la pantalla es pequeña o tiene demasiado zoom aplicar overflow-y: auto a la clase .menu.
### Interacción con los botones de burger and close.
1. Se necesita que cuando estemos en mobiles el display sea block
2. Aplicar al boton de "cerrar"la propiedad align-self: flex-end; 
3. Aplicar a ambos botones las siguientes propiedades: border:none; background-color: none; cursor:pointer;
4. Para que ambos tomen botones tomen la misma posición:
    1.  Aplicar opacity de 0.5 a la clase menu.
    2.  A la clase .cerrar-menu aplicar un padding de 20px 15px
5. Se requiere que el menu responsivo se vea al dar clip en el boton hamburguesa:
    1. Cambiar la opacity a cero.
    2. Cuando se muestre el boton de hamburguesa los elementos del navbar estan solamente opacos pero existen y por lo tanto se le puede hacer clip para que no existan se debe utilizar la propiedad} pointer-events: none; siempre en la clase .menu 
    3. Crear una clase que se llame ".menu_opened" con las propiedades opacity: 1; pointer-events: all;
    4. Un js se encargará de añadir o eliminar la clase ".menu_opened" al menu (&lt;ul&gt;) si tiene la clase esta abierto si no la tiene esta cerrado.
    5. linkear el js con defer.
    6. Crear tres variable 1°. "menu" que seleccione la clase ".menu" 2°. "openMenuBtn" que seleccione la clase ".open-menu" 3°. "closeMenuBtn" que seleccione la clase ".cerrar-menu"
    7. Crear una función llamada toggleMenu() que hará que el menu esta abierto que lo cierre y si cerrado que lo abra.
        1. Dentro de la función selecionar la variable menu..."le digo classList.toggle() y el toggle le va aplicar la clase .menu_opened a la clase"
        2. Asignar la función creada al evento onclick de los botones mediante la 2° y 3° variables creadas.
        * openMenuBtn.addEventListener("click", toggleMenu)
8. Para añadir una pequeña transición: en la clase ".menu" del @media query utilizar la propiedad transition: opacity 0.3s; (transiciona el opacity a 0.1s)


[Volver al Indice](index.md)
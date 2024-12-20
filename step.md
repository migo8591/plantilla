# Configuraciones generales: 
1. Utilizar etiqueta header para englobar el navbar con una clase "topheader".
2. Utilizar un segundo englobe con la etiqueta nav con una clase "topnav".
3. Para el logo: crear un enlace (<a>) con la clase logo dentro de este enlace van a ir 1) la imagen con height de 50 y width de 50 y 2) un div con el titulo del sitio.
4. Afuera del enlace se crea el menu con etiqueta <ul> y clase "menu" para crear los <li> li*4>a
5. shift + alt + 🠕🠗 → duplica y alt + 🠕🠗 → arrastra
6. Utilizar la libreria normalize (Hace que el sitio se vea igual en cualquier navegador)
7. Para agregar una fuente: 
    1. Ir a google font: el facilitador escoge Montserrat con los estilos Regular 400, Medium 500 y Bold 700
    2. Copiar el link correspondiente y pegar en visualStudio después de la etiqueta title.
8. Resetear los enlaces a none y agregar color
9. :root es un selector generico es igual a utilizar html en css.
# Creando la barra de navegación: 
1. en navbar.css a la clase topnav aplicar display: flex (df) con justify-content: 
space-between (jc). Aplicar un padding de 10px para que los elementos "tenga aire" con respecto a la ventana (espacio)
## Para el logo: 
2. para que la imagen y el nombre de la pagina esten en horizontal aplicar display:flex y align-items: center;
3. aplicar otros estilos como font-size, font-weight y color
4. Para redondear la imagen: .logo img {border-radius:50%}
## Para el menu:
1. Utilizar la clase menu y aplicar los estilos: display: flex, list-style: none (para quitar el punto), resetear el margin y el padding a cero, 
2. aplicar a la etiqueta li: padding: 0;
3. aplicar a la etiqueta a: color, font-size, font-weight, line-height (una forma de central el texto de forma horizontal)
## Para agregar una sombra a la barra:
1. a la clase topheader agregar el estilo box-shadow  0 4px 5 px #xxx (ejeX, ejeY, blur, color)
## Para evitar un ancho maximo:
1. Para lograr un tope: en la clase .topnav agregar el estilo max-width de 980px
2. Y para que este centrado con respecto al header: margin 0 auto; (margin: ⮁ ⇄)
## Para fijar la barra: 
1. A la clase topheader se debe aplicar los estilos: position: fixed; left: 0; top: 0;
2. Para recuperar el ancho de la barra: width: 100%
### Diseño para dispositivos mobiles: (26:50)

https://unedcr-my.sharepoint.com/personal/miguel_munoz_uned_cr/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmiguel%5Fmunoz%5Funed%5Fcr%2FDocuments%2F1%2FvideosMyFirstWebCV%2Fparte%201%5F%20Barra%20de%20navegaci%C3%B3n%20usando%20flexbox%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ea144b25f%2Da81a%2D4339%2D92a8%2Dc1a3477c11b3

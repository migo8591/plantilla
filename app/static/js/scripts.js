document.addEventListener("DOMContentLoaded", () =>{
    const menu2 = document.querySelector(".menu") //lista <ul>
    const openMenuBoton = document.querySelector(".open-menu") //btn hamburguesa
    const closeMenuBoton = document.querySelector(".cerrar-menu") //btn cerrar
    const navLinks = menu.querySelectorAll("a")//todos los enlaces del menu
    //Alterna estado del menu - aplica la clase:
    function stateMenu(){
        const isMenuOpened = menu2.classList.toggle("menu_test")
        console.log(isMenuOpened)
        testing(isMenuOpened)

    }
    //Comprobación:
    function testing(receive){
        if (receive){
            console.log(`El valor de isMenuOpened es  ${receive} y se muestra la x con los enlaces.`);
            
        }else{
            console.log(`El valor de isMenuOpened es  ${receive} y se muestra la h sin los enlaces.`);
            
        }

    }
    //Actualiza tabindex segun el estado del menu
    function updateTabIndexes(state){


    }

    openMenuBoton.addEventListener("click",stateMenu)
    closeMenuBoton.addEventListener("click",stateMenu)
})
//Definiendo la media query:
const mediaQuery = window.matchMedia("(max-width:980px)")
//función para actualizar la variable segun el estado de la media query:
function updateVariable(){
    const isSmallScreen = mediaQuery.matches//true si cumple la media or falso
    console.log("¿Pantalla pequeña?", isSmallScreen);
    return isSmallScreen
}
//inicializa la variable:
let screen = updateVariable()
const navLinks = menu.querySelectorAll("a")//todos los enlaces del menu

console.log(`valor de la variable screen: ${screen}`);
//Escucha cambios en el tamñaño de la ventana:
mediaQuery.addEventListener("change",()=>{
    screen =updateVariable()
})
if (screen){
    console.log("El tamaño de la pantalla es pequeño");
    console.log(navLinks);
    navLinks.forEach((link)=>{
        link.tabIndex = -1
    })

}else{
    console.log("El tamaño de la pantalla es grande");
}
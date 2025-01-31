console.log("funciona")

const menu = document.querySelector(".menu")
const openMenuBtn = document.querySelector(".open-menu")
const closeMenuBtn = document.querySelector(".cerrar-menu")

function toggleMenu(){
    menu.classList.toggle("menu_opened")
}

openMenuBtn.addEventListener("click",toggleMenu);
closeMenuBtn.addEventListener("click",toggleMenu);



function getArticleContent(){
    var content = CKEDITOR.instance['content-id']
    return content.getData()
}
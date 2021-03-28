ROOT = "http://127.0.0.1:8000/"

var adicionar = document.getElementsByClassName("box__imagem--adicionar")
var remover = document.getElementsByClassName("box__imagem--remover")
var lista_final = document.getElementsByClassName("lista__final-array")

var cont = 0;
var itens = [];


for (var i = 0; i < adicionar.length; i++) {
    adicionar[i].addEventListener("click", addItens)
}

for (var i = 0; i < adicionar.length; i++) {
    remover[i].addEventListener("click", remItens)
}

function addItens(evento) {

    cont++;
    
    evento.preventDefault();
    const nome = evento.path[2].getElementsByClassName('box__imagem--texto')[0].innerText;
    const preco = parseFloat(evento.path[2].getElementsByClassName('box__imagem--preco')[0].innerText.slice(2, 8).replace(",", "."));
    let item = [nome, preco];
    itens.push(item)
    console.log(itens)
    document.querySelector("[name='lista']").value = itens
}

function remItens(evento) {
    cont--;
    if (cont <= 0) {
        cont=0
    }

    evento.preventDefault();
    const nome = evento.path[2].getElementsByClassName('box__imagem--texto')[0].innerText;
    const preco = parseFloat(evento.path[2].getElementsByClassName('box__imagem--preco')[0].innerText.slice(2, 8).replace(",", "."));
       
    for (i =0; i <itens.length; i++){
        if (itens[i][0] === nome && itens[i][1] === preco) {
            itens.splice(i, 1);
            break;
        }
    }
    console.log(itens)
    document.querySelector("[name='lista']").value = itens
}
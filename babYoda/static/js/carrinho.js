var adicionar = document.getElementsByClassName('box__imagem--adicionar')
var remover = document.getElementsByClassName('box__imagem--remover')

var cont = 0;
var itens = [];


for (var i = 0; i < adicionar.length; i++) {
    adicionar[i].addEventListener("click", addItens)
}

for (var i = 0; i < remover.length; i++) {
    remover[i].addEventListener("click", remItens)
}

function addItens(evento) {
    cont++;
    document.getElementById("carrinho").style.display = 'block';
    evento.preventDefault();
    const nome = evento.path[2].getElementsByClassName('box__imagem--texto')[0].innerText;
    const preco = evento.path[2].getElementsByClassName('box__imagem--preco')[0].innerText;
    
    console.log(nome, preco);
}

function remItens() {
    cont--;
    if (cont <= 0) {
        cont=0
        document.getElementById("carrinho").style.display = 'none';
    }
}





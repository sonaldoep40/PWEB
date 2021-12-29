function remove(url) {
    var resultado = confirm("Você realmente deseja remover?");
    if (resultado==true)
        window.location.href = url;
}
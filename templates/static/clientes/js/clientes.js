function add_carro(){
    console.log()
    container = document.getElementById('form-carro')

    html = "<br><div class='row'><div class='col-md'><input type='text' placeholder='carro' class='from-control' name='carro'></div><div class='col-md'><input type='text' placeholder='Placa' class='from-control' name='placa'></div><div class='col-md' ><input type='number' placeholder='ano' class='form-control' name='ano'></div></div></br>"

    container.innerHTML += html
}

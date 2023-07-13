function guardar(){
    let tit = document.getElementById('titulo').value;
    let tip = document.getElementById('tipo').value;
    let g = document.getElementById('genero').value;
    let s = document.getElementById('sinopsis').value;
    let i = document.getElementById('imagen').value;
    let v = document.getElementById('valoracion').value;
    let vm = document.getElementById('valoracion_max').value;
    

        let contenido = {
            titulo: tit,
            tipo: tip,
            genero: g,
            sinopsis: s,
            imagen: i,
            valoracion: v,
            valoracion_max: vm
        };
    
    let url = 'http://127.0.0.1:5000/contenidos';
    let options = {
        body: JSON.stringify(contenido),
        method: 'POST',
        headers: {'Content-Type': 'application/json'} //le explica el tipo de dato que le llega.
    }

    fetch(url, options)
    .then(function(){
        alert("Contenido agregado satisfactoriamente"); //Sweetalert es mejor.
        window.location.href='./contenidos.html';
    })
    .catch(err=>{
        console.error(err);
        alert("Ocurrió un error. No se pudo agregar el contenido"); //Sweetalert es mejor.
    })
}

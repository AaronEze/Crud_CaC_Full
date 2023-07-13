//Recuperar datos URL y mostrar en los inputs
console.log(location.search);

let argsUrl = location.search.substring(1).split('&');
console.log(argsUrl);

let data = [];
for(let i = 0; i < argsUrl.length; i++) {
    data[i] = argsUrl[i].split('=');
}
console.log(data);

document.getElementById('id').value = decodeURIComponent(data[0][1])
document.getElementById('titulo').value = decodeURIComponent(data[1][1])
document.getElementById('tipo').value = decodeURIComponent(data[2][1])
document.getElementById('genero').value = decodeURIComponent(data[3][1])
document.getElementById('sinopsis').value = decodeURIComponent(data[4][1])
document.getElementById('imagen').value = decodeURIComponent(data[5][1])
document.getElementById('valoracion').value = decodeURIComponent(data[6][1])
document.getElementById('valoracion_max').value = decodeURIComponent(data[7][1])



//Actualizar los datos
function modificar(){
    let id = document.getElementById('id').value;
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

    let url = 'http://127.0.0.1:5000/contenidos/'+id;
    let options = {
        body: JSON.stringify(contenido),
        method: 'PUT',
        headers: {'Content-Type': 'application/json'} //le explica el tipo de dato que le llega.
    };

    fetch(url, options)
    .then(function(){
        alert('El contenido se editó exitosamente');
        window.location.href = './contenidos.html';
    })
    .catch(err=>{
        alert('No se pudo modificar.');
        console.error(err);
    })
}
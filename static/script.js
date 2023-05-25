var diametro = document.getElementById("diametro");
var botonCh = document.getElementById("calcular_ch");
var interior = document.getElementById("interior");
var exterior = document.getElementById("exterior");
var contenedor_imagen = document.getElementById("contenedor_imagen");
var imagen_chavetero = document.getElementById("imagen_cha");
var mayor = document.getElementById("mayor");
var menor = document.getElementById("menor");
var largo = document.getElementById("largo");
var grados = document.getElementById("grados");
var botonCono = document.getElementById("calcular_cono");

async function enviarDatos(datos){
	var mensaje = {
        	texto: datos
        };
        var priReps = await fetch(`${window.origin}/api`, {
        	method: "POST",
		credentials: "include",
		body: JSON.stringify(mensaje),
		cache: "no-cache",
		headers: new Headers({
			"content-type": "application/json"
		})
        });
	var segRes = await priReps.json();
	return segRes[0].respuesta;
};


botonCh.addEventListener('click', async ()=>{
	if(diametro.value != ""){
		if (interior.checked || exterior.checked){
			radio = "interior";
			diametroValor = diametro.value;
			if(interior.checked == false){
				radio = "exterior";
			};
			res = await enviarDatos(["chavetero",diametroValor,radio]);
			imagen_chavetero.src ="static/chli.jpg";
			var timestamp = new Date().getTime();
			imagen_chavetero.src = "static/imagen_chavetero.jpg?timestamp=" + timestamp;
		};
	};
});

botonCono.addEventListener('click', async ()=>{
    if (mayor.value === "" || menor.value === "" || largo.value === "") {
        alert("Por favor, completa todos los campos.");
        return;
    }
    if (isNaN(mayor.value) || isNaN(menor.value) || isNaN(largo.value)) {
        alert("Por favor, ingresa solo números válidos.");
        return;
    }
    res = await enviarDatos(["cono",mayor.value, menor.value, largo.value]);
    grados.textContent = res + "°";
});
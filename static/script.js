var diametro = document.getElementById("diametro");
var botonCh = document.getElementById("calcular_ch");
var interior = document.getElementById("interior");
var exterior = document.getElementById("exterior");
var contenedor_imagen = document.getElementById("contenedor_imagen");
var imagen_chavetero = document.getElementById("imagen_cha");

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

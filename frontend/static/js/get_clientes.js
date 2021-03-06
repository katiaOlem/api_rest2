function getClientes() {
//#libreria para conectarse con enpoints//
    var request = new XMLHttpRequest();
     //Accede a la session de la pagina
    usernombre = window.prompt('Usernombre:')
    password = window.prompt('Password:')
    //mandar el password y contraseña


    //url 
   //asincrona o false sincrona
    request.open('GET', "https://8000-katiaolem-apirest2-qwcr8ep7p9d.ws-us53.gitpod.io/clientes/");
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Authorization", "Basic " + btoa(usernombre + ":" + password))
    request.setRequestHeader("content-type", "application/json");
    
    const  tabla   = document.getElementById("tabla_clientes"); //donde vamos a estra trabajando///

    var tblBody = document.createElement("tbody");//creación de elementos//
    var tblHead = document.createElement("thead");
     //valores 
    tblHead.innerHTML = `
        <tr>
            <th>Detalle</th>
            <th>Actualizar</th>
            <th>Borrar</th>
            <th>ID Cliente</th>
            <th>Nombre</th>
            <th>Email</th>
        </tr>`;

    request.onload = () => {
        // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }
        
        else if (request.status == 202){
            const response = request.responseText;
            const json = JSON.parse(response);
            ///poner limite de los datos
            for (let i = 0; i < json.length; i++) {
                var tr          = document.createElement('tr');
                var detalle     = document.createElement('td');
                var actualizar  = document.createElement('td');
                var borrar      = document.createElement('td');
                var id_cliente  = document.createElement('td');
                var nombre      = document.createElement('td');
                var email       = document.createElement('td');
///lo que deseas hacer agragar, eliminar, borrar
                detalle.innerHTML       = "<a href='/templates/get_cliente.html?"+json[i].id_cliente+"'>Detalle</a";
                actualizar.innerHTML    = "<a href='/templates/update_clientes.html?"+json[i].id_cliente+"'>Actualizar</a";
                borrar.innerHTML        = "<a href='/templates/delete_clientes.html?"+json[i].id_cliente+"'>Borrar</a";
                id_cliente.innerHTML    = json[i].id_cliente;
                nombre.innerHTML        = json[i].nombre;
                email.innerHTML         = json[i].email;

                tr.appendChild(detalle);
                tr.appendChild(actualizar);
                tr.appendChild(borrar);
                tr.appendChild(id_cliente);
                tr.appendChild(nombre);
                tr.appendChild(email);
                
                tblBody.appendChild(tr);
            }
            tabla.appendChild(tblHead);
            tabla.appendChild(tblBody);
        }
    };
    request.send();
}
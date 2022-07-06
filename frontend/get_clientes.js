function getClientes(offset) {
    //#libreria para conectarse con enpoints//
     var request = new XMLHttpRequest();   
     //Accede a la session de la pagina //metodo get
     username= prompt("username");
     password= prompt("password");
     //mandar el password y contraseña
     
    //url 
   //asincrona o false sincrona
     request.open('GET', 'https://8000-katiaolem-apirest2-qwcr8ep7p9d.ws-us51.gitpod.io/clientes/', true);
     request.setRequestHeader("Accept", "application/json");
     request.setRequestHeader("Authorization", "Basic " + btoa(username + ":" + password))
     request.setRequestHeader("Content-Type", "application/json");
 
     const  tabla   = document.getElementById("tabla_clientes");  //donde vamos a estra trabajando
 
     var tblBody = document.createElement("tbody"); //creación de elementos
     var tblHead = document.createElement("thead");
 //valores 
     tblHead.innerHTML = `
         <tr>
             <th>Id Cliente</th>
             <th>Nombre</th>
             <th>Email</th>
         </tr>`;

     request.send();
 
     request.onload = () => {
         // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
         const response = request.responseText;
         const json = JSON.parse(response);
         console.log("Response " + response);
         console.log("Json " +  json);
         if (request.status === 401 || request.status === 403) {
             alert(json.detail);
             
         }
         else if (request.status == 202){
             console.log(request);
             const response = request.responseText; //almacenamos la lista
             
             const json = JSON.parse(response);
             ///poner limite de los datos
             for (let i = 0; i < json.length; i++) {
                 var tr = document.createElement('tr');
                 var id_cliente = document.createElement('td');
                 var nombre = document.createElement('td');
                 var email = document.createElement('td');
               
 ///lo que deseas hacer agragar, eliminar, borrar solo cambiando get_
                 id_cliente.innerHTML = json[i].id_cliente;
                 nombre.innerHTML = json[i].nombre;
                 email.innerHTML = json[i].email;
                 
 
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
 };

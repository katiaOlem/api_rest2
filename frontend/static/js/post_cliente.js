function PostCliente(){
//#libreria para conectarse con enpoints//
   
    usernombre  = window.prompt('Usernombre:')
    password    = window.prompt('Password:')
    //mandar el password y contraseña 

    let nombre = document.getElementById("nombre");
    let email  = document.getElementById("email");

    let payload = {
        "nombre": nombre.value,
        "email" : email.value,
    }

    console.log("nombre: " + nombre.value);
    console.log("email: "  + email.value);
    console.log(payload);
    
    var request = new XMLHttpRequest();   //Accede a la session de la pagina//
    //url 
   //asincrona o false sincrona
    request.open('POST', 'https://8000-katiaolem-apirest2-qwcr8ep7p9d.ws-us53.gitpod.io/clientes/',true);
    request.setRequestHeader("Content-Type", "application/json");
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Authorization", "Basic " + btoa(usernombre + ":" + password))
    

    
    request.onload = () => {
        
        const response  = request.responseText;
        const json      = JSON.parse(response);     
        const status    = request.status;

        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }

        else if (request.status == 202){

            console.log("Response: " + response);
            console.log("JSON: " + json);
            console.log("Status: " + status);

            alert(json.message);
            window.location.replace("/index.html")
        }
    };
    request.send(JSON.stringify(payload));
};
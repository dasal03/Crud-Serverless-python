function enviar(data) {
  console.log("Entro")

  fetch("https://qyrmwjgt2k.execute-api.us-east-1.amazonaws.com/", {
    mode: "no-cors",
    method: "POST", // or 'PUT'
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
    })
    .catch((error) => {
      console.log("Error:", error);
    });

}

const form = document.getElementById("form1");

console.log(form);

form.onsubmit = function(event) {

  event.preventDefault();
  
  producto = form.elements.producto.value;
  valor = form.elements.valor.value;
  modulo = form.elements.modulo.value;

  const data = {
    producto: producto,
    valor: valor,
    modulo: modulo
  };

  enviar(data);
  event.preventDefault();
}
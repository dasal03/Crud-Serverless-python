data = {
  producto: "dgrdgdgs",
  valor: "2000",
  modulo: "productos",
};

fetch("https://qyrmwjgt2k.execute-api.us-east-1.amazonaws.com/", {
  method: "POST", // or 'PUT'
  mode: "cors",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
})
  .then((response) => response.text())
  .then((data) => {
    console.log("Success:", data);
  });

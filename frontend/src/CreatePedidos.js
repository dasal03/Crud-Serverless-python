import React from "react";
import axios from "axios";

export default class PedidoList extends React.Component {
  datafrom = {};

  handleChange = (event) => {
    const { name, value } = event?.target;
    this.datafrom[name] = value;
  };

  handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post(
        `https://qyrmwjgt2k.execute-api.us-east-1.amazonaws.com/`,
        this.datafrom
      )
      .then((res) => {
        console.log(this.datafrom);
        console.log(res);
        console.log(res.data);
      });
  };

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input
            type="text"
            name="nombre"
            placeholder="Nombre"
            className="nombre"
            onChange={this.handleChange}
          />

          <input
            type="text"
            name="id_producto"
            placeholder="ID Producto"
            className="idproduct"
            onChange={this.handleChange}
          />

          <input
            type="text"
            name="cantidad"
            placeholder="Cantidad"
            className="cantidad"
            onChange={this.handleChange}
          />

          <input
            type="text"
            name="valor_total"
            placeholder="Valor Total"
            className="valtotal"
            onChange={this.handleChange}
          />

          <input
            type="text"
            name="direccion"
            placeholder="Dirección"
            className="direccion"
            onChange={this.handleChange}
          />

          <input
            type="text"
            name="ciudad"
            placeholder="Ciudad"
            className="ciudad"
            onChange={this.handleChange}
          />

          <input
            type="text"
            name="telefono"
            placeholder="Telefono"
            className="telefono"
            onChange={this.handleChange}
          />

          <input
            type="text"
            name="id_estado"
            placeholder="ID estado"
            className="idestado"
            onChange={this.handleChange}
          />

          <input
            type="text"
            name="modulo"
            placeholder="Modulo"
            className="modulo"
            onChange={this.handleChange}
          />
          <button type="submit" className="crear">
            Crear Pedido
          </button>
        </form>
      </div>
    );
  }
}

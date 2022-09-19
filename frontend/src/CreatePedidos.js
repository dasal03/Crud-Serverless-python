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
      <section class="form-contact">
        <header>
          <span>
            <i class="fa fa-paper-plane"></i>
          </span>
        </header>
        <form class="contact" onSubmit={this.handleSubmit}>
          <label for="nombre" class="nombre">
            Nombre
          </label>
          <input
            type="text"
            name="nombre"
            placeholder="Nombre"
            className="nombre"
            onChange={this.handleChange}
          />

          <label for="id_producto" className="id_producto">
            Producto
          </label>
          <input
            type="text"
            name="id_producto"
            placeholder="ID Producto"
            className="idproduct"
            onChange={this.handleChange}
          />

          <label for="cantidad" className="cantidad">
            Cantidad
          </label>
          <input
            type="text"
            name="cantidad"
            placeholder="Cantidad"
            className="cantidad"
            onChange={this.handleChange}
          />

          <label for="valor_total" className="valor_total">
            Valor total
          </label>
          <input
            type="text"
            name="valor_total"
            placeholder="Valor Total"
            className="valtotal"
            onChange={this.handleChange}
          />

          <label for="direccion" className="direccion">
            Direccion
          </label>
          <input
            type="text"
            name="direccion"
            placeholder="Dirección"
            className="direccion"
            onChange={this.handleChange}
          />

          <label for="ciudad" className="ciudad">
            Ciudad
          </label>
          <input
            type="text"
            name="ciudad"
            placeholder="Ciudad"
            className="ciudad"
            onChange={this.handleChange}
          />

          <label for="telefono" className="telefono">
            Telefono
          </label>
          <input
            type="text"
            name="telefono"
            placeholder="Telefono"
            className="telefono"
            onChange={this.handleChange}
          />

          <label for="id_estado" className="id_estado">
            Estado
          </label>
          <input
            type="text"
            name="id_estado"
            placeholder="ID estado"
            className="idestado"
            onChange={this.handleChange}
          />

          <label for="modulo" className="modulo">
            Modulo
          </label>
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
      </section>
    );
  }
}

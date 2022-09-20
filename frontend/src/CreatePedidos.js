import React, { useState } from "react";
import axios from "axios";

const ProductList = () => {
  let [form, setForm] = useState({ id_estado: "1", modulo: "pedidos" });

  const handleChange = (event) => {
    console.log(form);
    setForm({ ...form, [event.target.name]: event.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post(`https://qyrmwjgt2k.execute-api.us-east-1.amazonaws.com/`, form)
      .then((res) => {
        console.log(form);
        console.log(res);
        console.log(res.data);
        alert("Success!");
      });
  };

  return (
    <section className="form-contact">
      <header>
        <span>
          <i className="fa fa-paper-plane"></i>
        </span>
      </header>
      <form className="contact" onSubmit={handleSubmit}>
        <label for="nombre" className="nombre">
          Nombre
        </label>
        <input
          type="text"
          name="nombre"
          className="nombre"
          onChange={handleChange}
        />

        <label for="id_producto" className="id_producto">
          Producto
        </label>
        <select name="id_producto" id="producto" className="id_producto" onChange={handleChange}>
          <option value="options">Seleccione una opcion</option>
          <option value="1">Agua</option>
          <option value="2">Arequipe</option>
          <option value="3">Detodito</option>
          <option value="4">Vive 100</option>
          <option value="5">Bonyurt</option>
          
        </select>
        {/* <input
          type="text"
          name="id_producto"
          className="id_producto"
          onChange={handleChange}
        /> */}

        <label for="cantidad" className="cantidad">
          Cantidad
        </label>
        <input
          type="number"
          name="cantidad"
          className="cantidad"
          onChange={handleChange}
        />

        <label for="valor_total" className="valor_total">
          Valor total
        </label>
        <input
          type="number"
          name="valor_total"
          className="valtotal"
          onChange={handleChange}
        />

        <label for="direccion" className="direccion">
          Direccion
        </label>
        <input
          type="text"
          name="direccion"
          className="direccion"
          onChange={handleChange}
        />

        <label for="ciudad" className="ciudad">
          Ciudad
        </label>
        <input
          type="text"
          name="ciudad"
          className="ciudad"
          onChange={handleChange}
        />

        <label for="telefono" className="telefono">
          Telefono
        </label>
        <input
          type="number"
          name="telefono"
          className="telefono"
          onChange={handleChange}
        />

        <label for="id_estado" className="idestado">
          Estado
        </label>
        <input
          type="number"
          name="id_estado"
          className="idestado"
          value="1"
          onChange={handleChange}
        />

        <label for="modulo" className="modulo">
          Modulo
        </label>
        <input
          type="text"
          name="modulo"
          className="modulo"
          value="pedidos"
          onChange={handleChange}
        />
        <button type="submit" className="crear">
          Crear Pedido
        </button>
      </form>
    </section>
  );
};

/* export default class PedidoList extends React.Component {

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
        alert("Success!");
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
            className="nombre"
            onChange={this.handleChange}
          />

          <label for="id_producto" className="id_producto">
            Producto
          </label>
          <input
            type="text"
            name="id_producto"
            className="id_producto"
            onChange={this.handleChange}
          />

          <label for="cantidad" className="cantidad">
            Cantidad
          </label>
          <input
            type="number"
            name="cantidad"
            className="cantidad"
            onChange={this.handleChange}
          />

          <label for="valor_total" className="valor_total">
            Valor total
          </label>
          <input
            type="number"
            name="valor_total"
            className="valtotal"
            onChange={this.handleChange}
          />

          <label for="direccion" className="direccion">
            Direccion
          </label>
          <input
            type="text"
            name="direccion"
            className="direccion"
            onChange={this.handleChange}
          />

          <label for="ciudad" className="ciudad">
            Ciudad
          </label>
          <input
            type="text"
            name="ciudad"
            className="ciudad"
            onChange={this.handleChange}
          />

          <label for="telefono" className="telefono">
            Telefono
          </label>
          <input
            type="number"
            name="telefono"
            className="telefono"
            onChange={this.handleChange}
          />

          <label for="id_estado" className="id_estado">
            Estado
          </label>
          <input
            type="number"
            name="id_estado"
            className="idestado"
            onChange={this.handleChange}
          />

          <label for="modulo" className="modulo">
            Modulo
          </label>
          <input
            type="text"
            name="modulo"
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
} */

export default ProductList;

import React, { Component } from "react";
import { HashRouter as Router, Route, NavLink ,Link} from "react-router-dom";

import "./delivery.css";

class Delivery extends Component {
  render() {
    return (
      <div class="manager_main">
        <div class="header_manager">
            <div class="header_text">
              <h1>Delivery agent's Name</h1>
              <h2>Rating (Out of 5)</h2>
            </div>
        </div>
        <br></br>
        <h2 style={{color:"white",textAlign:"left", marginLeft:"20px",fontWeight:"bold"}}>Current order details</h2>
        <div class="delivery_table">
            <table class="table table-dark">
                <thead>
                    <tr>
                    <th scope="col">Customer name</th>
                    <th scope="col">Customer phone no.</th>
                    <th scope="col">Delivery address</th>
                    <th scope="col">Delivery Instr.</th>
                    <th scope="col">Order Summary</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <th scope="row">Pranjal</th>
                    <td>8837601071</td>
                    <td>yfavbjhu54653tyh,2jgwjb,981971</td>
                    <td>leave at doorstep</td>
                    <td>Dosa, idli, vada</td>
                    </tr>
                </tbody>
                </table>
                <button type="button" class="btn btn-success btn-lg">Delivered</button>
            </div>

        <div class="new">
          <div class="delivery_info">
              <h1 class="my_profile">My Profile</h1>
              <h2>Outlet</h2>
              <h2>Salary</h2>
              <h2>Bonus</h2>
              <h2>Attendance</h2>
          </div>
        </div>
      </div>
    );
  }
}

export default Delivery;

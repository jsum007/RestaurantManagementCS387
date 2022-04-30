import React, { Component } from "react";
import axios from 'axios'
import { HashRouter as Router, Route, NavLink ,Link} from "react-router-dom";

import "./manager.css";

class Manager extends Component {
  state = {
    menu_items: [],
    id:this.props.match.id
  }

  componentDidMount() {
    axios.get("http:/127.0.0.1:8000/fetch_menu")
      .then(res => {
        const menu_items = res.data;
       menu_items.filter(number => {
               if (number[3] === "South") {
      return true
          }
             return false
           })
        this.setState({ menu_items });
      })
  }
  render() {
    return (
      <div class="manager_main">
        <div class="header_manager">
            <div class="header_text">
              <h1>Manager's Name</h1>
              <h2>Outlet</h2>
            </div>
        </div>
        <br></br>
        <h2 style={{color:"white",textAlign:"left", marginLeft:"20px",fontWeight:"bold"}}>Staff info:</h2>
        <div class="manager_table">
            <table class="table table-dark">
                <thead>
                    <tr>
                    <th scope="col">Staff Id</th>
                    <th scope="col">Staff Name</th>
                    <th scope="col">Attendance</th>
                    <th scope="col">Base Salary</th>
                    <th scope="col">Bonus</th>
                    <th scope="col">Paycut</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <th scope="row">1</th>
                    <td>Mark</td>
                    <td>29</td>
                    <td>20000</td>
                    <td>2100</td>
                    <td>500</td>
                    </tr>
                    <tr>
                    <th scope="row">2</th>
                    <td>Jacob</td>
                    <td>27</td>
                    <td>28500</td>
                    <td>3130</td>
                    <td>800</td>
                    </tr>
                    <tr>
                    <th scope="row">3</th>
                    <td>Larry</td>
                    <td>25</td>
                    <td>22300</td>
                    <td>1100</td>
                    <td>400</td>
                    </tr>
                </tbody>
                </table>
            </div>
      </div>

    
    );
  }
}

export default Manager;

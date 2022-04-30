import React, { Component } from "react";
import { HashRouter as Router, Route, NavLink ,Link} from "react-router-dom";
import { Button } from "reactstrap";

import "./waiter.css";

class Waiter extends Component {
    constructor(props) {
        super(props);
    
        this.state={
        id: window.location.pathname.split('/')[window.location.pathname.split('/').length - 1]
        }
    
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
      }

    handleChange(event) {
        let target = event.target;
        let value = target.type === "checkbox" ? target.checked : target.value;
        let name = target.name;
    
        this.setState({
          [name]: value
        });
      }
    
      handleSubmit(event) {
        event.preventDefault();
    
        console.log("The form was submitted with the following data:");
        console.log(this.state);
      }

  render() {

    return (
      <div class="waiter_main">
        <div class="waiter_staff">
            <div class="header_text">
              <h1>Waiter's Name</h1>
              <h2>Outlet</h2>
            </div>
        </div>
        <br></br>
        <h2 style={{color:"white",textAlign:"left", marginLeft:"20px",fontWeight:"bold"}}>Generate bill:</h2>
        <div class="bill">
        <form className="formFields2" onSubmit={this.handleSubmit}>
          <div className="formField2">
            <label className="formFieldLabel2" htmlFor="email">
              <h3 style={{color:"white",textAlign:"left", marginLeft:"20px",marginTop:"20px",fontWeight:"bold"}}>Enter table id</h3>
            </label>
            <input
              type="table_id"
              id="table_id"
              className="formFieldInput2"
              placeholder="Table Id"
              name="table_id"
              value={this.state.id}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField2">
            <button className="formFieldButton2">Generate bill</button>{" "}
          </div>
        </form>
        </div>
        <br></br>
        <h2 style={{color:"white",textAlign:"left", marginLeft:"20px",fontWeight:"bold"}}>Dish Status:</h2>
        <div class="waiter_table">
            <table class="table table-dark">
                <thead>
                    <tr>
                    <th scope="col">Table Id</th>
                    <th scope="col">Dish Id</th>
                    <th scope="col">Status</th>
                    <th scope="col">Served?</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <th scope="row">1</th>
                    <td>23</td>
                    <td>Ordered</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">4</th>
                    <td>123</td>
                    <td>Preparing</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">1</th>
                    <td>23</td>
                    <td>Ordered</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">4</th>
                    <td>123</td>
                    <td>Preparing</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">9</th>
                    <td>3</td>
                    <td>Prepared</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">1</th>
                    <td>23</td>
                    <td>Ordered</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">4</th>
                    <td>123</td>
                    <td>Preparing</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">9</th>
                    <td>3</td>
                    <td>Prepared</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">1</th>
                    <td>23</td>
                    <td>Ordered</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">4</th>
                    <td>123</td>
                    <td>Preparing</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                    <tr>
                    <th scope="row">9</th>
                    <td>3</td>
                    <td>Prepared</td>
                    <td><button type="button" class="btn btn-success">Served</button></td>
                    </tr>
                </tbody>
                </table>
            </div>
      </div>

    
    );
  }
}

export default Waiter;

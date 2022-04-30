import React, { Component } from "react";
import { Link, NavLink } from "react-router-dom";
import {history} from 'history';
import axios from "axios"

class SignInForm_staff extends Component {
  constructor() {
    super();

    this.state = {
      id: "",
      password: "",
      role:'',
      uid:""
    };

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
    const article = { username: this.state.id,password:this.state.password };
    axios.post('http:/127.0.0.1:8000/login_staff', article)
        .then(response => this.setState({ ...this.state,role:response.data.role_assigned,uid:response.data.staff_id }));
  }
 




  render() {
    return (
      <div className="formCenter_p">
        <form className="formFields_p" onSubmit={this.handleSubmit}>
          <div className="formField_p">
            <label className="formFieldLabel_p" htmlFor="email">
              Staff Id
            </label>
            <input
              type="id"
              id="id"
              className="formFieldInput_p"
              placeholder="Enter your username"
              name="id"
              value={this.state.id}
              onChange={this.handleChange}
            />
          </div>

          <div className="formField_p">
            <label className="formFieldLabel_p" htmlFor="password">
              Password
            </label>
            <input
              type="password"
              id="password"
              className="formFieldInput_p"
              placeholder="Enter your password"
              name="password"
              value={this.state.password}
              onChange={this.handleChange}
            />
          </div>

          <div className="formField1_p">
          <button className="formFieldButton_p" type="submit">
          <Link
              to={this.state.role==""?"/chef/1":"/"+this.state.role+"/"+this.state.uid}>Sign In
            </Link></button>
          </div>

        </form>
      </div>
    );
  }
}

export default SignInForm_staff;

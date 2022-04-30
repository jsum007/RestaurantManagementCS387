import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from 'axios'

class SignUpForm extends Component {
  constructor() {
    super();

    this.state = {
      email: "",
      uname:"",
      password: "",
      name: "",
      h_address :"",
      h_pin:"",
      o_pin:"",
      o_address :"",
      phone:"",
      hasAgreed: false,
      u:""
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

  handleSubmit() {

    console.log(this.state);
    const article = { username: this.state.id, password: this.state.password };
    axios.post('//localhost:8000/register_customer', {username:this.state.uname,password:this.state.password,name:this.state.name,home_address:this.state.h_address,home_pincode:this.state.h_pin,work_address:this.state.work_address,work_pin:this.state.work_pin,mail_id:this.state.email,phone:this.state.phone})
        .then((response) => {window.localStorage.setItem('myid',String(response.data.customer_id));this.setState({...this.state,u:response.data.customer_id})});
    console.log(this.state.uid);
    console.log("jkjkjkjkk");

}


  render() {
    return (
      <div className="formCenter">
        <form onSubmit={this.handleSubmit} className="formFields">
          <div className="formField">
            <label className="formFieldLabel" htmlFor="name">
              Full Name
            </label>
            <input
              type="text"
              id="name"
              className="formFieldInput"
              placeholder="Enter your full name"
              name="name"
              value={this.state.name}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="uname">
              Username
            </label>
            <input
              type="uname"
              id="uname"
              className="formFieldInput"
              placeholder="Enter your username"
              name="uname"
              value={this.state.uname}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="password">
              Password
            </label>
            <input
              type="password"
              id="password"
              className="formFieldInput"
              placeholder="Create password"
              name="password"
              value={this.state.password}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="email">
              E-Mail Address
            </label>
            <input
              type="email"
              id="email"
              className="formFieldInput"
              placeholder="Enter your email address"
              name="email"
              value={this.state.email}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="phone">
              Phone No.
            </label>
            <input
              type="phone"
              id="phone"
              className="formFieldInput"
              placeholder="Enter your Phone No."
              name="phone"
              value={this.state.phone}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="h_address">
              Home Address
            </label>
            <input
              type="h_address"
              id="h_address"
              className="formFieldInput"
              placeholder="Enter your home address"
              name="h_address"
              value={this.state.h_address}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="h_pin">
              Home Pincode
            </label>
            <input
              type="h_pin"
              id="h_pin"
              className="formFieldInput"
              placeholder="Enter your office address"
              name="h_pin"
              value={this.state.h_pin}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="o_address">
              Office Address
            </label>
            <input
              type="o_address"
              id="o_address"
              className="formFieldInput"
              placeholder="Enter your office address"
              name="o_address"
              value={this.state.o_address}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="o_pin">
              Office Pincode
            </label>
            <input
              type="o_pin"
              id="o_pin"
              className="formFieldInput"
              placeholder="Enter your office pincode"
              name="o_pin"
              value={this.state.o_pin}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField1">
           <Link to={"/customer/"+String(this.state.u)}> <input className="formFieldButton"type="submit"/></Link>
            <Link to="/login_/sign-in" className="formFieldLink_">
              I'm already member
            </Link>
          </div>
        </form>
      </div>
    );
  }
}
export default SignUpForm;

import React, { Component } from "react";
import { BrowserRouter as Router, Route, NavLink,Switch } from "react-router-dom";
import SignInForm_staff from "./signInForm_staff";
import axios from "axios"
import "./loginStaff.css";

class LoginStaff extends Component {
  render() {
    return (
        <div className="Appi_p">
          <div className="appAside_p" />
          <div className="appForm_p">
            <div className="formTitle_p">
                Sign In
            </div>
            <SignInForm_staff />
          </div>
          <div className="appAside_p" />
        </div>
   
    );
  }
}

export default LoginStaff;

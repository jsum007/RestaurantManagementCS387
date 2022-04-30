import React, { Component } from "react";
import { HashRouter as Router, Route, NavLink ,Link} from "react-router-dom";

import "./chef.css";

class Chef_history extends Component {

 state={
   myid:this.props.match.params.id
 }
  render() {
    return (
      <div class="chef_main">
        <div class="header_staff">
            <div class="header_text">
              <h1>Chef's Name</h1>
              <h2>Expertise</h2>
              <h3>Rating</h3>
            </div>
        </div>
        <br></br>
        <h2 style={{color:"white",textAlign:"left", marginLeft:"20px",fontWeight:"bold"}}>Dish history</h2>
          
      </div>

    
    );
  }
}

export default Chef_history;

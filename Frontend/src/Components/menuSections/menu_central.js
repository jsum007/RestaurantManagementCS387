import React, { Component } from "react";
import { HashRouter as Router, Route, NavLink, Link } from "react-router-dom";
import { Button } from "reactstrap";
import axios from 'axios'
import "./menu.css";

class Menu_central extends Component {
    state = {
      menu_items: []
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
          <div className="Items">
            {this.state.menu_items.map(element=>{
                return (<div><div>{element[1]}</div>
                {element[4]=='1' || element[4]==1 ? <div style={{borderRadius: '50%',width:'20px',height:'20px',backgroundColor:'green'}}></div>:<div style={{borderRadius: '50%',width:'20px',height:'20px',backgroundColor:'red'}}></div>}
                  </div>)
            })}
        </div>
        );
    }
}

export default Menu_central;
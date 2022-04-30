import React, { Component } from "react";
import { HashRouter as Router, Route, NavLink, Link } from "react-router-dom";
import axios from 'axios'
import { Button } from "reactstrap";

import "./menu.css";

class Menu_south extends Component {
    state = {
        menu_items: []
    }

    componentDidMount() {
        axios.get("http://localhost:8000/fetch_menu")
            .then(res => {
                var menu_items = res.data;
                menu_items = menu_items.filter(number => {
                    if (number[3] === "South") {
                        return true
                    }
                    return false
                });
                console.log(menu_items);
                this.setState({ menu_items });
            })
    }

    render() {
        return ( <div className = "Items" >
          <h1 style={{color:"white",textDecoration:"underline", marginBottom:"40px"}}>South Indian</h1>
                {
                    this.state.menu_items.map(element => {
                            return ( < div >
                            { element[5] == '1' || element[5] == 1 ? < div style = { { marginRight:"8px",borderRadius: '50%',display: "inline-block", width: '10px', height: '10px',backgroundColor: 'green' }} > </div>:<div style={{ marginRight:"8px",borderRadius: '50%',display: "inline-block",width:'10px',height:'10px',backgroundColor:'red'}}>
                          </div >
                        }  
                            < div style={{marginBottom:"20px",color:"white",width:"40%",height:"50px",borderRadius:"5%",fontSize:"1.9em",backgroundColor:"orange",display: "inline-block", marginLeft:"0"}}> { element[1] } 
                            </div> 
                            
                        <button type="button" class="btn btn-light btn-sml" style={{display: "inline-block", marginLeft:"30px"}}>Add to cart</button>
                        </div>)
                    })
            } </div>
    );
}
}

export default Menu_south;
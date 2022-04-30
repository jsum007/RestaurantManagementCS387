import React, { Component } from "react";
import { HashRouter as Router, Route, NavLink, Link } from "react-router-dom";
import axios from 'axios'
import { Button } from "reactstrap";

import "./menu.css";

class Menu_north extends Component {
    state = {
        menu_items: [],
        cart:[],
        quantity:[]
    }

    componentDidMount() {
        axios.get("http://localhost:8000/fetch_menu")
            .then(res => {
                var menu_items = res.data;
                menu_items = menu_items.filter(number => {
                    if (number[3] === "North") {
                        return true
                    }
                    return false
                });
                this.setState({ menu_items });
            })
    }

    render() {
        return ( < div className = "Items" >
            <h1 style = {
                { color: "white", textDecoration: "underline", marginBottom: "40px" }
            } > North Indian </h1> {
            this.state.menu_items.map(element => {
                    return ( < div > {
                            element[5] == '1' || element[5] == 1 ? < div style = {
                                { marginRight: "8px", borderRadius: '50%', display: "inline-block", width: '10px', height: '10px', backgroundColor: 'green' }
                            } > </div>:<div style={{ marginRight:"8px",borderRadius: '50%',display: "inline-block",width:'10px',height:'10px',backgroundColor:'red'}}> </div >
                        } < div style = {
                            { marginBottom: "20px", color: "white", width: "40%", height: "40px", borderRadius: "5%", fontSize: "1.9em", backgroundColor: "orange", display: "inline-block", marginLeft: "0" }
                        } > { element[1] } </div> 

                        
                        <button type = "button"
                        class = "btn btn-light btn-sml"
                        style = {
                            { display: "inline-block", marginLeft: "30px" }
                        }
                        onClick = {
                            () => { var e=0;var i;for( i=0;i<this.state.cart;i++){
                                if(this.state.cart[i]==element[0]){
                                    var r=this.state.quantity;
                                    r[i]++;
                                    this.setState({...this.state,
                                        quantity:r}) ;e=1;break;
                                }
                            }
                        if(e==0){
                           var r=this.state.quantity;
                            r.push(1);
                           var w=this.state.cart;
                           w.push(element[0]);
                            this.setState({...this.state,
                                quantity:r
                                ,cart:w
                            })
                        }
                        }
                        } > Add to cart </button> </div > )
                    })
            } 
            <button type="button" class= "btn btn-light" onClick={()=>{
                axios.post("//localhost:8000/place_order",{dishes:this.state.cart,quantity:this.state.quantity,customer_id:window.localStorage.getItem('myid'),table_id:-1,outlet_id:window.localStorage.getItem('outlet_id')}).then(
                    (response)=>{
                        console.log(response.data.order_id);
                        window.localStorage.setItem('order_id',String(response.data.order_id));
                    }
                )
            }}>Place Order</button>
            </div>
        );
    }
}

export default Menu_north;
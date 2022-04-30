import React, { Component } from "react";
import { HashRouter as Router, Route, NavLink, Link } from "react-router-dom";

import "./chef.css";

class Chef_preparing extends Component {
    state = {
        myid: window.location.pathname.split('/')[window.location.pathname.split('/').length - 1]
    }
    render() {
        return ( <
            div class = "chef_main" >
            <
            div class = "header_staff" >
            <
            div class = "header_text" >
            <
            h1 > Chef 's Name</h1> <
            h2 > Expertise < /h2> <
            h3 > Rating < /h3> <
            /div> <
            /div> <
            br > < /br> <
            h2 style = {
                { color: "white", textAlign: "left", marginLeft: "20px", fontWeight: "bold" } } > Dish being prepared..... < /h2> <
            div class = "dish_tile" >
            Dish <
            /div> <
            div class = "left" >
            <
            Link to = "/chef" > < button type = "button"
            class = "btn btn-secondary" > Ready to serve! < /button></Link >
            <
            /div>  <
            div class = "chef_info" >
            <
            h1 class = "my_profile" > My Profile < /h1> <
            h2 > Outlet < /h2> <
            h2 > Salary < /h2> <
            h2 > Bonus < /h2> <
            h2 > Attendance < /h2> <
            Link class = "linnk"
            to = "chef_history" > Dish history < /Link> <
            /div>  <
            /div>


        );
    }
}

export default Chef_preparing;
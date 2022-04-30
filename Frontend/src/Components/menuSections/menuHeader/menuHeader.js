import React from 'react';
import  './menuHeader.css';
import {NavLink, Link} from 'react-router-dom';
import MenuAll from '../menuAll/menuAll';
import Footer from '../../navigation/footer/footer';
const menuHeader=(props)=>{
    return(
        <div>
        <section className="menuHeader">
        {props.children}
        <p className="menuTitle">MENU</p>
        <ul>
            <li>
                <NavLink  to="/">Home</NavLink>
            </li>
            <li>
                <NavLink  to="/menu">Menu </NavLink>
            </li>
        </ul>
        </section>
        <h1 style={{textDecoration:"underline"}}>Cuisine</h1>
        {/* <section className="menu-options">
            <MenuAll adding={props.adding} data={props.data}/>
        </section> */}
        <Link to="/menu_north"><button type="button" class="btn btn-lg btn-outline-success menu_btn">North</button></Link>
        <Link to="/menu_south"><button type="button" class="btn btn-lg btn-outline-success menu_btn">South</button></Link>
        <Link to="/menu_east"><button type="button" class="btn btn-lg btn-outline-success menu_btn">East</button></Link>
        <Link to="/menu_west"><button type="button" class="btn btn-lg btn-outline-success menu_btn">West</button></Link>
        <Link to="/menu_central"><button type="button" class="btn btn-lg btn-outline-success menu_btn">Central</button></Link>
        <Footer/>
        </div>
    );
}

export default menuHeader;
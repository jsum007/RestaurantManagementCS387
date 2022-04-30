import React, { Component } from 'react';
import './Offer.css';
import Toolbar from '../../Components/navigation/toolbar/toolbar';
import { NavLink,Link } from 'react-router-dom';
import {Container,Row,Col} from 'reactstrap';
import Tile from '../../Components/sections/section-tiles/tile/tile';
import Footer from '../../Components/navigation/footer/footer';
import axios from 'axios'

class Offer extends Component {
    state={
        tables:[]
    }
    componentDidMount() {
        axios.post('//localhost:8000/assign_outlet', {customer_id:parseInt(window.localStorage.getItem('myid')),is_delivery:0,pincode:""})
            .then((response) => {window.localStorage.setItem('outlet_id',String(response.data.outlet_id));
            console.log(response.data.outlet_id);
        axios.post('//localhost:8000/available_table',{outlet_id:response.data.outlet_id}).then((r)=>{
        this.setState({...this.state,tables:r.data.available_tables});
        console.log(r.data.available_tables)
        })
        });
        
 
     }
    render() {
        let temp;
    const extractor=(obj)=>{
         temp=Object.keys(obj).map(name=>obj[name]);
    }
    extractor(this.props.data.cards);
        return (
            <div className="Offer">
                <section className="Offers">
                    <Toolbar count={this.props.count} />
                    <p className="OffersHead">Dine In</p>
                    <div>
                        <NavLink to="/" style={{color:"white"}}>Home</NavLink>
                        <NavLink to="/menu">Menu</NavLink>
                    </div>
                </section>
                {this.state.tables.map((data)=>{
                    return (<div style={{color:'white',backgroundColor:'orange'}}>
                        {data}
                        <Link to="/menu"><button onClick={()=>{
                            axios.post("//localhost:8000/choose_table",{outlet_id:window.localStorage.getItem('outlet_id'),table_id:parseInt(data)})
                        }} style={{fontSize:'10px'}}> Choose this table</button></Link>
                    </div>)
                })}
               
                <Footer count={this.props.count}/>
            </div>
        );
    }
}

export default Offer;
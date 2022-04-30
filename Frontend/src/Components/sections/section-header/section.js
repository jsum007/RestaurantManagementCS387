import React, { Component } from 'react';
import './section.css';
import Brand from '../../miscelleous/brand/brand';
import GrabBtn from '../../buttons/grab-offer/grab-btn';
import Tiles from '../section-tiles/tiles/tiles';
import Specs from '../section-specs/specs';
import SpecOffer from '../spec-offer/specOffer';
import Stacked from '../stacked-photos/stacked';
import Footer from '../../navigation/footer/footer';
import axios from 'axios'

let back = <Brand />;
class section1 extends Component {
    state = {
        cls1: "circle",
        cls2: "circle",
        cls3: "circle",
        brand: false,
        customer_id:"",
        customer_name:"",
    }
    componentDidMount() {
       if( window.location.pathname.split('/').length>2){
        console.log("34wewerwr");
        axios.post('//localhost:8000/get_customer_details', {customer_id:window.location.pathname.split('/')[2]})
            .then((response) => {this.setState({...this.state,customer_id: response.data.customer_id,customer_name:response.data.customer_name });window.localStorage.setItem('myid',window.location.pathname.split('/')[2]);});
         
       }
        setTimeout(() => this.clickBtn(1), 30);

    }
    clickBtn(valv) {
        if (valv === 1) {
            back = <Brand show />;

            this.setState({ cls2: "circle" });
            this.setState({ cls3: "circle" });
            this.setState({ cls1: "full" });
        }
        else if (valv === 2) {

            this.setState({ cls3: "circle" });
            this.setState({ cls1: "circle" });
            this.setState({ cls2: "full" });
        }
        else if (valv === 3) {
            this.setState({ cls1: "circle" });
            this.setState({ cls2: "circle" });
            this.setState({ cls3: "full" });
        }
    }
    render() {
        return (
            <div style={{ overflowY: "hidden" }}>
                <section className="Header">
                    {this.props.children}
                    {back}
                   {window.location.pathname.split('/').length<=2 && <div className="button-offer">
                        <GrabBtn url="/login_staff" content="Login(staff)" />
                    </div>}
                    {window.location.pathname.split('/').length<=2 &&<div className="button-offer">
                        <GrabBtn url="/login_" content="Login(customer)" />
                    </div>}
                    {window.location.pathname.split('/').length>2 && <div className="button-offer" style={{color:'white',fontSize:'24px'}}>{"Welcome "+this.state.customer_name}</div>}
                    <div className="controls">
                        <div className="internal-c">
                            
                        </div>
                    </div>
                </section>
                <section className="sec-tiles">
                    <Tiles data={this.props.data.cards} />
                </section>
                <section className="specs">
                    <Specs />
                </section>
                <section className="specOffer">
                    <SpecOffer data={this.props.data.mainoffer} />
                </section>
                <section className="sec-stacked">
                    <Stacked />
                </section>
                {/* <section className="sec-map">
                </section> */}
                <Footer />
                {/* <section>
        <div style={{width:" 100%"}}>
        <iframe src="https://maps.google.com/maps?width=100%&height=600&hl=en&q=Malet%20St%2C%20London%20WC1E%207HU%2C%20United%20Kingdom+(Your%20Business%20Name)&ie=UTF8&t=&z=14&iwloc=B&output=embed" style={{height:"50vh",width:"100vw"}}><a href="https://www.mapsdirections.info/en/custom-google-maps/">Create a custom Google Map</a> by <a href="https://www.mapsdirections.info/en/">Measure area on map</a></iframe></div><br />
        </section> */}
            </div>
        );
    }

}
export default section1;
import React from 'react';
import './stacked.css';
import {Container,Row,Col} from 'reactstrap';
import rest from '../../../Assests/images/stacked/rest.jpeg';
import rest1 from '../../../Assests/images/stacked/rest1.jpeg';
import rest2 from '../../../Assests/images/stacked/rest2.jpeg';
import rest3 from '../../../Assests/images/stacked/rest3.jpeg';


const stacked=()=>{
    return(
            <div className="stacked-container">
            <p className="stackedTop">GALLERY</p>
            <Container>
                <Row>
                    <Col>
                    <div className="stacked">
                        <img src={rest1} alt="Stacked for restaurant!" />
                        </div>
                    </Col>
                    <Col>
                    <div  className="stacked"> 
                        <img src={rest} alt="Stacked for restaurant!"/>
                        </div>
                    </Col>
                    <Col>
                    <div className="stacked">
                        <img src={rest2} alt="Stacked for restaurant!"/>
                        </div>
                    </Col>
                    <Col >
                    <div className="stacked">
                        <img src={rest3} alt="Stacked for restaurant!"/>
                        </div>
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default stacked;
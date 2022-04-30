import React from 'react';
import './brand.css';

const brand=(props)=>{
    let vclass=" ";
    if(props.show){
        vclass="show";
    }
    let all_class=["brand"];
    all_class.push(vclass);
    return(
        <div className={all_class.join(" ")}>
            <p className="brandnum">Anti</p>
            <p className="name">SOCIAL</p>
            <div className="image-container">
            </div>
            <p className="lastTitle">A foodie's Indian paradise</p>
        </div>

    );
}

export default brand;
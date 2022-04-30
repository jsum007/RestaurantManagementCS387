import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from 'axios'

class SignInForm extends Component {
    constructor() {
        super();

        this.state = {
            id: "",
            password: "",
            uid: ""
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        let target = event.target;
        let value = target.type === "checkbox" ? target.checked : target.value;
        let name = target.name;

        this.setState({
            [name]: value
        });
    }

    handleSubmit() {

        console.log(this.state);
        const article = { username: this.state.id, password: this.state.password };
        axios.post('//localhost:8000/login_customer', article)
            .then(response => this.setState({...this.state, uid: response.data.customer_id }));
        console.log(this.state.uid);
        console.log("jkjkjkjkk");

    }

    render() {
        return ( <
            div className = "formCenter_p" >
            <
            form className = "formFields_p"
            onSubmit = { this.handleSubmit() } >
            <
            div className = "formField_p" >
            <
            label className = "formFieldLabel_p"
            htmlFor = "email" >
            Staff Id < /label>  <
            input type = "id"
            id = "id"
            className = "formFieldInput_p"
            placeholder = "Enter your username"
            name = "id"
            value = { this.state.id }
            onChange = { this.handleChange }
            />  < /
            div >

            <
            div className = "formField" >
            <
            label className = "formFieldLabel"
            htmlFor = "password" >
            Password <
            /label> <
            input type = "password"
            id = "password"
            className = "formFieldInput"
            placeholder = "Enter your password"
            name = "password"
            value = { this.state.password }
            onChange = { this.handleChange }
            /> < /
            div >

            <
            div className = "formField1_p" >
            <
            Link to = { this.state.uid == "" ? "/" : "/customer/" + this.state.uid } >
            <
            input className = "formFieldButton_p"
            type = "submit" / >
            <
            /Link> < /
            div >

            <
            /form> < /
            div >
        );
    }
}

export default SignInForm;
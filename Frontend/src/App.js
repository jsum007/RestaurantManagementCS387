import React, { Component } from 'react';
import './App.css';
import {BrowserRouter} from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';

import AllClass from './Containers/AllClass/AllClass';
class App extends Component {
 
  render() {
    
    return (
      <BrowserRouter>
      <div className="App">
      <AllClass/>
      </div>
      </BrowserRouter>
    );
  }
}

export default App;

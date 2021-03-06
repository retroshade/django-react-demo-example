import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
          <button type="button" onClick={this.onClick}>Send GET /products </button>
      </div>
    );
  }

  onClick(ev) {
      console.log("Sending a GET API Call!!!");
      axios.get('/products').then(res => {
          console.log(res)
      }).then(response => {
          console.log(JSON.stringify(response));
      })
  }
}

export default App;

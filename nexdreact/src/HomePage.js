import React, { Component } from 'react';
import './App.css';
import logo from "./NexdMovieClear.png"

export default class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      userName: '',      
    };
    this.handleButtonClick = this.handleButtonClick.bind(this);
  }

  handleInputChange = (event) => {
    this.setState({
      userName: event.target.value,
       // set displayUsername to false whenever the input field is changed
    });
  }

  handleButtonClick(){
    const requestOptions = {
        method: 'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({
            userName: this.state.userName
        })
    };
    fetch('/MovieApp/create-user', requestOptions).then((response)=>
    response.json()
    ).then((data)=> console.log(data));
  }

  render() {
    return (
      <div className="App">
        <header className="App-Title">
          <img src={logo} alt="logo" height = "150" width="200"/>
        </header>
        <header className="App-header">
          <p>
            Insert Letterboxd Username: &nbsp;
          </p>
          <input type="text" onChange={this.handleInputChange} />
          <button onClick={this.handleButtonClick}>
            Enter Username
          </button>
        </header>
        <body className="App-Body">
        </body>
      </div>
    );
  }
}



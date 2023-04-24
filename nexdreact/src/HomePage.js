import React, { Component } from 'react';
import './App.css';
import logo from "./NexdMovieClear.png";
import {MagnifyingGlass} from 'react-loader-spinner';




export default class HomePage extends Component {
  
  constructor(props) {
    super(props);
    this.state = {    
      isLoading: false, // new state variable
      userName: '',    
      moviePosters:['','','','',''],
      movieTitles: [],
      noviePosters: ['https://image.tmdb.org/t/p/w300/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg', 'https://image.tmdb.org/t/p/w300/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg', 'https://image.tmdb.org/t/p/w300/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg', 'https://image.tmdb.org/t/p/w300/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg','https://image.tmdb.org/t/p/w300/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg'], // an array of empty image sources  
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

    this.setState({
      moviePosters: ['','','','',''],
      movieTitles: [],
      isLoading: true
    });

    const requestOptions = {
        method: 'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({
            userName: this.state.userName
        })
    };
    fetch('/MovieApp/create-user', requestOptions).then((response)=>
    response.json()
    ).then((data)=> {
      const moviePosters = [];
      const movieTitles = [];
      for (const movie in data.movie_reccs_dict){
        const posterURL = 'https://image.tmdb.org/t/p/w300' + data.movie_reccs_dict[movie];
        moviePosters.push(posterURL);
        movieTitles.push(movie);
      }
      this.setState({ moviePosters, movieTitles, isLoading: false });
      console.log(data)
    });
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
          {this.state.isLoading ?
            <div>
            <MagnifyingGlass color="#00BFFF" height={80} width={80} />
            <p>Your NexdMovies are coming right up!</p>
            </div> :
            this.state.moviePosters.map((poster, index) => (
              <div key={index} style={{ margin: '20px' }}>
                <img src={poster} alt={`movie poster ${index}`} style={{width:'30vw', height:'45vh', maxWidth: '95%', overflow: 'hidden'}} />
                <p>{this.state.movieTitles[index]}</p>
              </div>
            ))
          }
        </body>
      </div>
    );
  }
  
}



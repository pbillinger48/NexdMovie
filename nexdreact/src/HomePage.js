import React, { Component } from 'react';
import './App.css';

import {MagnifyingGlass} from 'react-loader-spinner';




export default class HomePage extends Component {
  
  constructor(props) {
    super(props);
    this.state = {    
      isLoading: false, // new state variable
      userName: '',    
      movieTitles: [],
      moviePosters: [], // an array of empty image sources  
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
    if (!this.state.userName.trim()) {
      // if the input field is empty or contains only whitespace characters
      return;
    }
    this.setState({
      moviePosters: ['','','','',''],
      movieTitles: [],
      movieIDSURL: [],
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
      const movieIDSURL = [];
      const movies = Object.entries(data.reccs_info_dict).slice(-5);
        for (const [movie, info] of movies) {
          const posterURL = 'https://image.tmdb.org/t/p/w300' + info['poster'];
          moviePosters.push(posterURL);
          movieTitles.push(movie);
          movieIDSURL.push('https://letterboxd.com/tmdb/' + info['id']);
        }
        this.setState({ moviePosters, movieTitles, movieIDSURL, isLoading: false });
        console.log(data)
    });
  }

  handleRefreshClick = () =>{
    if (!this.state.userName.trim()) {
      // if the input field is empty or contains only whitespace characters
      return;
    }
    this.setState({
      moviePosters: ['','','','',''],
      movieTitles: [],
      movieIDSURL: [],
      isLoading: true
    });
    const requestOptions = {
      method: 'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({
          userName: this.state.userName
      })
    };
    fetch('/MovieApp/refresh-user', requestOptions)
      .then((response) => response.json())
      .then((data) => {
        const moviePosters = [];
        const movieTitles = [];
        const movieIDSURL = [];
        const movies = Object.entries(data.reccs_info_dict).slice(-5);
        for (const [movie, info] of movies) {
          const posterURL = 'https://image.tmdb.org/t/p/w300' + info['poster'];
          moviePosters.push(posterURL);
          movieTitles.push(movie);
          movieIDSURL.push('https://letterboxd.com/tmdb/' + info['id']);
        }
        this.setState({ moviePosters, movieTitles, movieIDSURL, isLoading: false });
        console.log(data)
      });      
  }

  handleShowMoreClick = () => {
    if (!this.state.userName.trim()) {
      // if the input field is empty or contains only whitespace characters
      return;
    }
    this.setState({
      moviePosters: ['','','','',''],
      movieTitles: [],
      movieIDSURL: [],
      isLoading: true
    });
    const requestOptions = {
      method: 'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({
        userName: this.state.userName
      })
    };
    fetch('/MovieApp/get-more', requestOptions)
      .then((response) => response.json())
      .then((data) => {
        const moviePosters = [];
        const movieTitles = [];
        const movieIDSURL = [];
        const movies = Object.entries(data.reccs_info_dict).slice(-5);
        for (const [movie, info] of movies) {
          const posterURL = 'https://image.tmdb.org/t/p/w300' + info['poster'];
          moviePosters.push(posterURL);
          movieTitles.push(movie);
          movieIDSURL.push('https://letterboxd.com/tmdb/' + info['id']);
        }    
        if (JSON.stringify(Object.keys(data.reccs_info_dict)) === JSON.stringify(Object.keys(data.movie_reccs_dict))){
          alert('No more NexdMovies left, rate more movies on Letterboxd for more!')
        }   
        this.setState({
          moviePosters,
          movieTitles,
          movieIDSURL,
          isLoading: false
        });
        
        console.log(data);
      })
      .catch((error) => console.error(error));
  }

  render() {
    return (
      <div className="App">
        <header className="App-Title">
          <p height="260"> </p>
        </header>
        <header className="App-header">
          <p className="App-font">Insert Letterboxd Username: &nbsp;</p>
          <input className="App-input" type="text" onChange={this.handleInputChange} />
          <button onClick={this.handleButtonClick} className="App-button">Enter Username</button>
        </header>
        <body className="App-Body">
          {this.state.isLoading ? (
            <div>
              <MagnifyingGlass color="#00BFFF" height={80} width={80} />
              <p className="App-font">Your NexdMovies are coming right up!</p>
            </div>
          ) : this.state.moviePosters.length === 0 ? (
            <p className="App-font">Your NexdMovies will be displayed here!</p>
          ) : (
            <>
              {this.state.moviePosters.map((poster, index) => (
                <div key={index} style={{ margin: "20px" }}>
                  <a href={this.state.movieIDSURL[index]}>
                    <img className ="App-Poster"
                      src={poster}
                      style={{
                        width: "30vw",
                        height: "45vh",
                        maxWidth: "95%",
                        overflow: "hidden",
                      }}
                    />
                  </a>
                  <p className="App-font">{this.state.movieTitles[index]}</p>
                </div>
              ))}
              <div style={{ margin: "20px"}}>
                {this.state.moviePosters.length > 0 && this.state.isLoading === false && (
                  <div>
                  <button className="App-button" onClick={this.handleShowMoreClick}>Show More </button>
                  <button className="App-button" onClick={this.handleRefreshClick}>Refresh </button>
                  </div>
                )}
              </div>
            </>
          )}
        </body>
      </div>
    );
  }
  
  
}



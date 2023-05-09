import React from "react";
import './App.css';
import logo from "./NexdMovieClear.png";
const About = () => {
  return (
    <div className="App">
        <header className="App-header">
            <div>
            <h1>
                Welcome to NexdMovie
            </h1>            
            </div>
        </header>
        <body className="App-Body">
            <div>
            <img src={logo} alt="logo" height="400" />        
            <p>NexdMovie is a site that takes Letterboxd user movie ratings and gives relevant ratings accordingly.</p>
            <p>To use your account, go to your letterboxd film page and look for the name in the https://letterboxd.com/YOURUSERNAMEHERE/films/</p>
            <p>Thank You!</p>
            <p>-Parker Billinger</p>
            </div>
        </body>
     
    </div>
  );
};
 
export default About;

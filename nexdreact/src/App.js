import logo from './logo.svg';
import './App.css';
import{ useState } from 'react';
function App() {
  const[username, setUsername] = useState('');
  const [displayUsername, setDisplayUsername] = useState('');

  const handleInputChange = (event) => {
    setUsername(event.target.value);
  };
  const handleButtonClick = () => {
    setDisplayUsername(username);
  }
  return (
    <div className="App">
      <header className="App-Title">
        <h1>
          NexdMovie
        </h1>
      </header>
      <header className="App-header">      
        <p>
          Insert Letterboxd Username: &nbsp;
        </p>
        <input type= "text" value={username} onChange={handleInputChange}/>
        
        <button onClick={handleButtonClick}>
        Enter Username
        </button>
      </header>
      <body className="App-Body">
        <p>{displayUsername}</p>
      </body>
    </div>
  );
}

export default App;

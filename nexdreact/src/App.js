import logo from './logo.svg';
import './App.css';

function App() {
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
        <input type= "text"/>
        
        <button>
        Enter Username
        </button>
      </header>
      <body className="App-Body">
        <p>test</p>
      </body>
    </div>
  );
}

export default App;

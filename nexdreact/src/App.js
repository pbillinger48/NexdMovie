import './App.css';
import Navbar from './Components/Navbar';
import { BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import HomePage from"./HomePage";
import About from './About'
function App() {  
  return (
    //<HomePage/>
    <Router>
    <Navbar />
    <Routes>
        <Route exact path='/' element={<HomePage />} />
        <Route path='/about' element={<About/>} />
    </Routes>
    </Router>
  );
}

export default App;

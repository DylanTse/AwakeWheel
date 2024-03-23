import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'; // Import Link from react-router-dom
import Dashboard from './Components/Dashboard';
import Photos from './Components/Photos';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/photos">Photos</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/photos" element={<Photos />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

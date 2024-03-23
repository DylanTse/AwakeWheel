import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Dashboard from './Dashboard';
import Photos from './Photos';

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
              <Link to="/data">Photos</Link>
            </li>
          </ul>
        </nav>

        <Route path="/" exact component={Dashboard} />
        <Route path="/data" component={Photos} />
      </div>
    </Router>
  );
}

export default App;

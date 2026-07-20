## frontend/src/App.js

import React from 'react';
import { Link } from 'react-router-dom';

const App = () => {
  return (
    <div>
      <h1>Ticket Management System</h1>
      <nav>
        <ul>
          <li><Link to="/login">Login</Link></li>
          <li><Link to="/register">Register</Link></li>
          <li><Link to="/tickets">Tickets</Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default App;

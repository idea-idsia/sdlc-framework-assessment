## frontend/src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from './App';
import LoginPage from './components/LoginPage';
import RegisterPage from './components/RegisterPage';
import TicketList from './components/TicketList';
import TicketDetail from './components/TicketDetail';

ReactDOM.render(
  <Router>
    <Switch>
      <Route exact path="/" component={App} />
      <Route path="/login" component={LoginPage} />
      <Route path="/register" component={RegisterPage} />
      <Route path="/tickets" component={TicketList} />
      <Route path="/ticket/:id" component={TicketDetail} />
    </Switch>
  </Router>,
  document.getElementById('root')
);

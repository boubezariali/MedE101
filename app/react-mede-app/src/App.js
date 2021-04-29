import React, { useState, Component } from 'react';
import { Container, Header } from 'semantic-ui-react';
import './App.css';
import { DiagnosisDisplay } from './components/DiagnosisDisplay';
import { FeatureSelector } from './components/FeatureSelector';

import { BrowserRouter as Router, Route, Switch, Link, Redirect } from "react-router-dom";
// Pages
import MainPage from "./pages/home";
import DiagnosisPage from "./pages/diagnosisPage";
import GamePage from "./pages/gamePage";
import NotFoundPage from "./pages/404"

function App() {
  return (
    <Router>
      <Switch>
        {/*all our routes here*/}
        <Route exact path="/" component={MainPage} />
        <Route exact path="/diagnosis" component={DiagnosisPage} />
        <Route exact path="/game" component={GamePage} />
        <Router exact path="/404" component={NotFoundPage} />
        <Redirect to="/404" />
      </Switch>
    </Router>
  );
}

export default App;

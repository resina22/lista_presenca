import React from 'react';
import {
  BrowserRouter as Router,
  Switch, Route,
} from "react-router-dom";
import 'normalize.css';

import Header from './components/header/header';
import notFound from './components/httpError/notFound';
import List from './attendance/list';
import Home from './home/home';

function App() {
  return (
    <div>
      <Router>
        <Header />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/attendances/:id/:date" component={List} />
          <Route path="*" component={notFound} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;

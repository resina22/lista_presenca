import React from 'react';
import { Link } from "react-router-dom";

import './header.css';
import logo from '../../assert/logo.svg';
import Button from '../button/button'

function Header() {
  return (
    <div>
      <header
        className="top-bar"
      >
        <div className="row align-items-center container">

          <div className="column">
            <img src={logo} className="logo" alt="Logo"/>
          </div>

          <div className="column">
            <Link to="/">
              <Button text="Disciplinas" type="primary rounded" />
            </Link>
          </div>

        </div>
      </header>
    </div>
  );
}

export default Header;

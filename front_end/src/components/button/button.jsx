import React from 'react';

import './button.css';

function Button(props) {
  const { type, text } = {...props};
  const classButton =  `button ${type}`;
  return (
    <button className={ classButton }>{ text }</button>
  );

}

export default Button;

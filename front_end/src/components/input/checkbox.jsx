import React from 'react';

import './input.css';

function Checkbox(props) {  
  return (
    <div>
      <label>{ props.label || 'Não informado!' }</label>
      <input
        type='checkbox'
        {...props}
        className='input checkbox'
      />
    </div>
  )
}

export default Checkbox;

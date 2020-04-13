import React from 'react';

function Text(props) {
  return (
    <input
      type='text'
      className='input text'
      {...props}
    />
  )
}

export default Text;

import React from 'react'

import './alert.css';

function Alert(props) {
    const {text, type} = {...props}
    return createAlert(text, type)
}

function createAlert(text, type) {
    return (
        <div className={`alert ${type || ''} text-center`}>
            {text}
        </div>
    )
}

export default Alert;

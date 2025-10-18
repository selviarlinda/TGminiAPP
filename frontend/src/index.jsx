import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

// Код инициализации React должен быть здесь, а не внутри компонента
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
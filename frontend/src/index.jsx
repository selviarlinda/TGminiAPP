import React from 'react';
import ReactDOM from 'react-dom/client';
import { WebAppProvider } from '@twa-dev/sdk/react';
import './index.css';
// ИЗМЕНЯЕМ ИМПОРТ, ЧТОБЫ УКАЗАТЬ НА ПРАВИЛЬНЫЙ ФАЙЛ .jsx
import App from './App.jsx';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <WebAppProvider>
      <App />
    </WebAppProvider>
  </React.StrictMode>
);
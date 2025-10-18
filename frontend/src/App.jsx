import React from 'react';
import { useWebApp } from '@twa-dev/sdk/react';
import './App.css';

function App() {
  const { initDataUnsafe } = useWebApp();
  const user = initDataUnsafe?.user;

  return (
    <div className="App">
      <header className="App-header">
        <h1>Моё Крипто ТМА</h1>
        {user ? (
          <div>
            <p>Привет, {user.first_name} {user.last_name}!</p>
            <p>Ваш ID: {user.id}</p>
            <p>Username: @{user.username}</p>
          </div>
        ) : (
          <p>Пожалуйста, откройте это приложение в Telegram.</p>
        )}
      </header>
    </div>
  );
}

export default App;
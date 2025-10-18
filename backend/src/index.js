// Импортируем установленные библиотеки
const express = require('express');
const cors = require('cors');
const crypto = require('crypto');
require('dotenv').config({ path: '../../.env' }); // Загружаем переменные из .env в корне проекта

// --- КЛЮЧЕВАЯ ФУНКЦИЯ БЕЗОПАСНОСТИ ---
// Эта функция проверяет, что данные пришли именно от Telegram, а не от мошенника.
function validateInitData(initData, botToken) {
  const urlParams = new URLSearchParams(initData);
  const hash = urlParams.get('hash');
  urlParams.delete('hash');
  
  // Собираем все поля в одну строку для проверки хеша
  const dataCheckString = Array.from(urlParams.entries())
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([key, value]) => `${key}=${value}`)
    .join('\n');

  // Создаем секретный ключ из токена бота
  const secretKey = crypto.createHmac('sha256', 'WebAppData').update(botToken).digest();
  
  // Генерируем хеш из данных и сравниваем его с хешем от Telegram
  const calculatedHash = crypto.createHmac('sha256', secretKey).update(dataCheckString).digest('hex');

  // Если хеши совпадают, данные подлинные
  return calculatedHash === hash;
}

// Создаем приложение Express
const app = express();

// Включаем CORS, чтобы фронтенд мог делать запросы к бэкенду
app.use(cors());
// Включаем парсинг JSON-тела запросов
app.use(express.json());

// Загружаем токен бота из переменных окружения
const BOT_TOKEN = process.env.BOT_TOKEN;
if (!BOT_TOKEN) {
  console.error('BOT_TOKEN не найден! Пожалуйста, добавьте его в файл .env');
  process.exit(1);
}

// --- НАШ ПЕРВЫЙ API ЭНДПОИНТ ---
// Он будет принимать initData, проверять их и возвращать данные пользователя
app.post('/api/validate', (req, res) => {
  const { initData } = req.body;

  if (!initData) {
    return res.status(400).json({ error: 'initData не предоставлены' });
  }

  // Запускаем нашу функцию проверки
  const isValid = validateInitData(initData, BOT_TOKEN);

  if (isValid) {
    console.log('Данные от Telegram успешно верифицированы!');
    const params = new URLSearchParams(initData);
    const user = JSON.parse(params.get('user'));
    
    // Если все хорошо, отправляем клиенту данные пользователя и статус OK
    res.status(200).json({
      message: 'Данные валидны',
      user: {
        id: user.id,
        firstName: user.first_name,
        lastName: user.last_name,
        username: user.username,
      },
    });
  } else {
    // Если проверка провалилась, отправляем ошибку
    console.warn('Попытка подделки данных!');
    res.status(403).json({ error: 'Невалидные данные от Telegram' });
  }
});

// Определяем порт для сервера
const PORT = process.env.BACKEND_PORT || 5000;

// Запускаем сервер
app.listen(PORT, () => {
  console.log(`Сервер бэкенда запущен на порту ${PORT}`);
});

# --- ЭТАП 1: СБОРКА ФРОНТЕНДА ---
FROM node:18-alpine AS builder
WORKDIR /app

# Копируем package.json И НАШ НОВЫЙ package-lock.json
COPY ../frontend/package.json ../frontend/package-lock.json ./

# ИСПОЛЬЗУЕМ 'npm ci' ВМЕСТО 'npm install'
# 'ci' (Clean Install) устанавливает зависимости СТРОГО по package-lock.json,
# что гарантирует воспроизводимость сборки и решает нашу проблему.
RUN npm ci

# Копируем все остальные файлы фронтенда
COPY ../frontend/ ./

# Запускаем сборку
RUN npm run build


# --- ЭТАП 2: НАСТРОЙКА NGINX ---
FROM nginx:1.21-alpine

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/dist /usr/share/nginx/html
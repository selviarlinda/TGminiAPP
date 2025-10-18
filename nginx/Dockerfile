# --- ЭТАП 1: СБОРКА ФРОНТЕНДА ---
FROM node:18-alpine AS builder
WORKDIR /app

# Путь от корня проекта: frontend/package.json
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

# Путь от корня проекта: frontend/
COPY frontend/ ./
RUN npm run build

# --- ЭТАП 2: НАСТРОЙКА NGINX ---
FROM nginx:1.21-alpine

# Путь от корня проекта: nginx/nginx.conf
COPY nginx/nginx.conf /etc/nginx/nginx.conf

COPY --from=builder /app/dist /usr/share/nginx/html
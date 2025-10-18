# --- ЭТАП 1: Сборка приложения с Vite ---
FROM node:18-alpine AS build
WORKDIR /usr/src/app

COPY package.json ./
RUN npm install
COPY . .

# Запускаем сборку через Vite
RUN npm run build

# --- ЭТАП 2: Раздача статики ---
FROM nginx:1.21-alpine
# Копируем из папки /dist, а не /build
COPY --from=build /usr/src/app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
FROM node:16-alpine as builder
WORKDIR '/usr/src/app/frontend'
COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx
COPY --from=builder /usr/src/app/frontend/build /usr/share/nginx/html
FROM node:14

WORKDIR /usr/src/app/server

COPY package.json package-lock.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["node", "server.js"]
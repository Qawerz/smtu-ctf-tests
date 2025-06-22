FROM node:24-alpine as build-stage
WORKDIR /app
COPY package.json ./app/package.json
RUN npm install
COPY . .
# RUN npm run build
EXPOSE 80
CMD ["npm", "run", "dev"]
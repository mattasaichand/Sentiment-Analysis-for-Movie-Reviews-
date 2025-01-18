FROM node:18

WORKDIR /frontend

# Copy all files (including package.json) from local frontend folder to container's /frontend folder
COPY . /frontend

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]


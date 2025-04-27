FROM node:23

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY . ./

RUN yarn run build

RUN yarn install --production

EXPOSE 5500

ENV NODE_ENV=production
ENV PORT=5500
ENV HOSTNAME="0.0.0.0"

CMD ["yarn", "run", "start"]
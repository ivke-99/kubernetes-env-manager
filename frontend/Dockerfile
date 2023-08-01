# Stage 0, based on Node.js, to build and compile Angular
FROM node:18.0.0 as node
WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm install --silent
COPY ./src /app/src
COPY ./public /app/public
COPY ./vite.config.js /app/
RUN npm run build

# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
# FROM nginx:alpine
FROM byjg/nginx-extras:1.21
# ARG APP_VERSION
# ENV ENV_VERSION $APP_VERSION
COPY --from=node /app/dist/ /usr/share/nginx/html
COPY config/env.sh /usr/share/nginx/html
COPY config/nginx.conf /etc/nginx/conf.d/default.conf
WORKDIR /usr/share/nginx/html/
# RUN sed -i "s/env-config.js/$(echo env-config_${ENV_VERSION}.js)/" index.html
RUN mv /usr/share/nginx/html/index.html /usr/share/nginx/html/index-${RANDOM}.html
RUN sed -i "s/index.html/$(ls | grep index)/" /etc/nginx/conf.d/default.conf
COPY config/start.sh /
RUN chmod -R +rw /usr/share/nginx/html

# Add bash
RUN apk add --no-cache bash
CMD ["/start.sh"]
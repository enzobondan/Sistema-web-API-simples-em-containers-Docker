FROM nginx:alpine

RUN mkdir -p /usr/share/nginx/html/static

COPY . /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
FROM nginx:alpine

RUN mkdir -p /usr/share/nginx/html/static

COPY form.html /usr/share/nginx/html/
COPY listagem.html /usr/share/nginx/html/

COPY style.css /usr/share/nginx/html/static/
COPY script_form.js /usr/share/nginx/html/static/
COPY script_listagem.js /usr/share/nginx/html/static/

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
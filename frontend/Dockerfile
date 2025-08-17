FROM nginx:alpine

# Criar diretório para arquivos estáticos
RUN mkdir -p /usr/share/nginx/html/static

# Copiar arquivos HTML
COPY form.html /usr/share/nginx/html/
COPY listagem.html /usr/share/nginx/html/

# Copiar arquivos estáticos (CSS, JS)
COPY style.css /usr/share/nginx/html/static/
COPY script_form.js /usr/share/nginx/html/static/
COPY script_listagem.js /usr/share/nginx/html/static/
COPY env.js /usr/share/nginx/html/static/

# Configuração do Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
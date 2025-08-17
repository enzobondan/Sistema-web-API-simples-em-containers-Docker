#!/bin/sh

mkdir -p /usr/share/nginx/html/static

cat <<EOF > /usr/share/nginx/html/static/env.js
window._env_ = {
  API_URL: "$API_URL"
};
EOF

nginx -g 'daemon off;'

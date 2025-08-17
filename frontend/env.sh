cat <<EOF > /usr/share/nginx/html/static/env.js
window._env_ = {
  API_URL: "$API_URL"
}
EOF

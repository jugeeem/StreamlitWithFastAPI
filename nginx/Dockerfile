FROM nginx:1.27.2-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY init.sh /usr/local/bin/init.sh
RUN chmod +x /usr/local/bin/init.sh

CMD ["init.sh"]

FROM nginx:stable-alpine

# Remove default nginx config and copy our custom config
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
FROM nginx

COPY nginx.conf /etc/nginx/conf.d/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# RUN apt update
# RUN apt upgrade
# RUN apt install certbot python3-certbot-nginx
# RUN certbot --nginx -d fpforce2.net -d www.fpforce2.net

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
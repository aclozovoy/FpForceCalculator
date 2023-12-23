FROM nginx

COPY nginx.conf /etc/nginx/conf.d/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

RUN apt update
RUN apt upgrade
RUN apt install -y certbot 
RUN apt install -y python3-certbot-nginx
# RUN certbot --nginx -d fpforce.net -d www.fpforce.net

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
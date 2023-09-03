 FROM nginx:alpine

 COPY nginx.conf /etc/nginx/conf.d/nginx.conf
 RUN rm /etc/nginx/conf.d/default.conf

#  EXPOSE 80 8000

 CMD ["nginx", "-g", "daemon off;"]
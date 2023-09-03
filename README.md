# FpForceCalculator

[FpForce.net](http://fpforce.net/)

ASCE 7-22 Nonstructural Seismic Force Calculator

Web app built with Flask to simplify calculation of nonstructural seismic force.


      - ./data/nginx:/etc/nginx/conf.d


  



       command: "/bin/sh -c 'while :; do sleep 6h & wait $${!}; nginx -s reload; done & nginx -g \"daemon off;\"'"



  certbot:
    image: certbot/certbot

    volumes:
      - ./data/certbot/conf:/etc/letsencrypt
      - ./data/certbot/www:/var/www/certbot
    entrypoint: "/bin/sh -c 'trap exit TERM; while :; do certbot renew; sleep 12h & wait $${!}; done;'"




    server {
    listen 443 ssl;
    server_name fpforce_test.net;
    server_tokens off;

    ssl_certificate /etc/letsencrypt/live/fpforce_test.net/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/fpforce_test.net/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass  http://localhost:8081;
        proxy_set_header    Host                $http_host;
        proxy_set_header    X-Real-IP           $remote_addr;
        proxy_set_header    X-Forwarded-For     $proxy_add_x_forwarded_for;
    }
}




    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }





          - ./data/certbot/conf:/etc/letsencrypt
      - ./data/certbot/www:/var/www/certbot




                      proxy_redirect http://backend/ https://$server_name/;




upstream backend {
    server 127.0.0.1:8080;
}

host="0.0.0.0", port=8000


                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $host;
                proxy_set_header X-NginX-Proxy true;
                proxy_redirect off;
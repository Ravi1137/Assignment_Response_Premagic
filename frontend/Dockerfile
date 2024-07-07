# Use the official Nginx image
FROM nginx:alpine

# Copy the content of the current directory to the default Nginx public folder
COPY . /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# CMD directive is not necessary for Nginx, as it runs automatically

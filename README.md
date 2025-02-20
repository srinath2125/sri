[**Static Site Server**](https://github.com/srinath2125/srinath2125/)


This project focuses on two key technologies: Nginx for efficient web serving and rsync for seamless file synchronization between your local development environment and the remote server.

**Step 1- Register and setup a remote Linux server on GCP :-**

    •     Log in to your GCP account.
      
    •     Go to the Ccompute ENGINE dashboard.
      
    •     Click "Launch a VM Instance."
      
    •     Assign a name e.g. Static Site
      
    •     Choose an Ubunto AMI .
      
    •     Select e2-micro (2 vCPUs, 1 GB Memory) instance type (free tier eligible).
      
    •     Create a new key pair, download it, and keep it safe.
      
    •     Configure instance details (use default settings for now).
      
    •     Configure security group:
      
    •     Allow HTTP & HTTPS in Firewalls.
      
    •     Launch instance.




**Step 2- Install and Configure Nginx to Serve a Static Site :-**

Nginx is a high-performance web server suitable for serving static content.

    Install Nginx:

    On Ubuntu/Debian systems:

sudo apt update
sudo apt install nginx -y

Start and Enable Nginx:

sudo systemctl start nginx
sudo systemctl enable nginx

**Configure Nginx to Serve Your Static Site:**

By default, Nginx serves files from /var/www/html. You can modify this by editing the default server block or creating a new one.

    sudo nano /etc/nginx/sites-available/default

Update the root directive to point to your site's directory:

server {
    listen 80;
    server_name your_domain_or_ip;

    root /var/www/your_site;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

Replace /var/www/your_site with the path to your site's directory and your_domain_or_ip with your domain name or server IP address.

    Create the Site Directory and Set Permissions:

sudo mkdir -p /var/www/your_site
sudo chown -R $USER:$USER /var/www/your_site


Test and Reload Nginx Configuration:

    sudo nginx -t
    sudo systemctl reload nginx



**Step 3:- Create a Simple Webpage with Basic HTML, CSS, and Image Files**

Develop your website using HTML, CSS, and any necessary images. Place your index.html and associated files in your site's directory (/var/www/your_site).


**1. Develop Your Website Using HTML, CSS, and Images :-**

Begin by creating the necessary files for your website:

    HTML File (index.html): This file serves as the main page of your website.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Simple Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
    </header>
    <main>
        <p>This is a simple webpage created with HTML and CSS.</p>
        <img src="images/sample-image.jpg" alt="Sample Image">
    </main>
    <footer>
        <p>&copy; 2025 My Simple Website</p>
    </footer>
</body>
</html>

**2. CSS File (styles.css): This file contains the styles for your HTML elements :-**

    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        text-align: center;
    }

    header, footer {
        background-color: #f8f8f8;
        padding: 20px;
    }

    main {
        padding: 20px;
    }

    img {
        max-width: 100%;
        height: auto;
    }

    Image File: Place any images you want to include in an images directory. For example, images/sample-image.jpg.

**3. Place Your Files in the Site's Directory :-**

On your server, create a directory to host your website files. The default directory for Nginx is /var/www/html, but you can create a new directory if desired:

sudo mkdir -p /var/www/your_site

Replace your_site with your preferred directory name.

Next, upload your index.html, styles.css, and images folder to this directory.

**4. Configure Nginx to Serve the Static Site :-**

Modify the Nginx configuration to serve your static website:

    Edit the Default Configuration File:

sudo nano /etc/nginx/sites-available/default

Update the Configuration:

Replace the existing server block with the following, or modify it to match your setup:

    server {
        listen 80;
        server_name your_domain_or_ip;

        root /var/www/your_site;
        index index.html;

        location / {
            try_files $uri $uri/ =404;
        }
    }

Replace your_domain_or_ip with your domain name or server's IP address, and /var/www/your_site with the path to your site's directory.

    Test and Reload Nginx:

    sudo nginx -t
    sudo systemctl reload nginx

This will apply the new configuration and start serving your static site.


**Step 4:- Use rsync to Update the Remote Server with the Local Static Site**

To streamline updates to your website, use rsync within a deployment script.

    Generate SSH Keys (If Not Already Done):

    On your local machine:

    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

This creates a public/private key pair.

    Copy the Public Key to Your Server and create a file <authorized_keys>in server under ~/.ssh/
    and paste the public key in the file.    

once its done now change the 
This allows passwordless SSH authentication.

    Create the Deployment Script (deploy.sh):

    On your local machine, create a script to sync your local site directory with the server:

    #!/bin/bash

    # Variables
    LOCAL_DIR="/path/to/your/local/site/"
    REMOTE_USER="username"
    REMOTE_HOST="your_server_ip"
    REMOTE_DIR="/var/www/your_site/"

    # Sync files
    rsync -avz --delete -e "ssh" $LOCAL_DIR $REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR

    echo "Deployment complete."

Replace the placeholders with your actual paths and server details.

    Make the Script Executable:

chmod +x deploy.sh

Run the Deployment Script:

    ./deploy.sh

This script uses rsync to synchronize your local site files with the server, ensuring that any changes are reflected online.

**4. Point Your Domain to the Server**

If you have a domain name, update its DNS settings to point to your server's IP address. This process varies depending on your domain registrar. Once DNS propagation is complete, your site will be accessible via your domain name

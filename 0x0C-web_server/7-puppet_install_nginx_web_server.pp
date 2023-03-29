# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Start Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Set up Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "server {
    listen 80;
    server_name _;
    location / {
      return 301 http://$host/redirect_me;
    }
    location /redirect_me {
      return 301 https://www.google.com/;
    }
  }",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Reload Nginx service
exec { 'nginx_reload':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
}


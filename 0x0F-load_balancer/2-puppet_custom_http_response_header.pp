#This is to use puppet to automate the creation of custom http header
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"\${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}

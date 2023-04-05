class { '::nginx':
  confd_purge => false,
  confd_dir   => '/etc/nginx/conf.d',
}

nginx::resource::server { 'default':
  listen_port => 80,
  location    => '/',
  add_header  => ['X-Served-By $hostname'],
}


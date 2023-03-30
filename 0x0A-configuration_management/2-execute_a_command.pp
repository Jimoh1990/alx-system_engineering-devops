#Executes a bah 
class myclass {
  exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin:/usr/sbin:/bin:/sbin',
    onlyif  => 'pgrep killmenow',
  }
}

include myclass


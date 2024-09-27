#!/usr/bin/pup

class install_flask {

  # Ensure pip3 is installed
  package { 'python3-pip':
    ensure => installed,
  }

  # Install Flask version 2.1.0
  exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    path    => ['/usr/bin', '/usr/sbin'],
    unless  => '/usr/bin/pip3 show flask | grep "Version: 2.1.0"',
    require => Package['python3-pip'],
  }

}


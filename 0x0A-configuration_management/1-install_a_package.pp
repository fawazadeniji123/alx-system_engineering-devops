#!/usr/bin/pup

# Ensure Python3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
python::pip { 'Flask':
  ensure   => '2.1.0',
  pip_provider => 'pip3',
}

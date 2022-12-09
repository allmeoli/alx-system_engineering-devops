# install puppet from pip3
package { ['python3-pip3']:
  ensure => installed,
}

package { 'pip3':
  require  => Package['python3-pip3'],
  ensure   => latest,
  provider => 'pip3',
}
package { 'Flask':
  ensure   => installed,
  require  => Package['pip3'],
  name     => 'Flask~=2.1.0',
  provider => 'pip3',
}

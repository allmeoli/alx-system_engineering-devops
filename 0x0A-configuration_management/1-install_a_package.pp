# install puppet from pip3

package { 'flask':
  ensure   => '2.1.0',
  require  => Package['pip3'],
  name     => 'flask~=2.1.0',
  provider => 'pip3',
}

# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"

  # Forward Flask
  # config.vm.network "forwarded_port", guest: 8001, host: 8001, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"
  config.vm.network "private_network", ip: "192.168.33.10"

  # Provider-specific configuration
  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
    vb.cpus = 1

    # Fixes some DNS issues on some networks
    # vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    # vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

  # Copy your .gitconfig file so that your git credentials are correct
  if File.exists?(File.expand_path("~/.gitconfig"))
    config.vm.provision "file", source: "~/.gitconfig", destination: "~/.gitconfig"
  end

  # Copy your ssh keys for github so that your git credentials work
  if File.exists?(File.expand_path("~/.ssh/id_rsa"))
    config.vm.provision "file", source: "~/.ssh/id_rsa", destination: "~/.ssh/id_rsa"
  end
  if File.exists?(File.expand_path("~/.ssh/id_rsa.pub"))
    config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/id_rsa.pub"
  end

  # Copy your .vimrc file so that your VI editor looks right
  if File.exists?(File.expand_path("~/.vimrc"))
    config.vm.provision "file", source: "~/.vimrc", destination: "~/.vimrc"
  end

  ######################################################################
  # Setup a Python development environment
  ######################################################################
  config.vm.provision "shell", inline: <<-SHELL
    sudo -H -u vagrant sh -c "echo 'export SPACE=dev' >> ~/.bashrc"

    apt-get update
    apt-get install -y git zip tree python-pip python-dev
    apt-get -y autoremove
    pip install --upgrade pip

    # Install app dependencies
    cd /vagrant
    sudo pip install -r requirements.txt
  SHELL

  ######################################################################
  # Add CouchDB docker container
  ######################################################################
  config.vm.provision "shell", inline: <<-SHELL
    sudo mkdir -p /opt/couchdb/data
    sudo chown vagrant:vagrant /opt/couchdb/data
  SHELL

  # Add CouchDB docker container
  # docker run -d --name couchdb -p 5984:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=pass couchdb
  config.vm.provision "docker" do |d|
    d.pull_images "couchdb"
    d.run "couchdb",
      args: "--restart=always -d --name couchdb -p 5984:5984 -v /opt/couchdb/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=pass"
  end
end

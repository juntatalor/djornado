# -*- mode: ruby -*-
# vi: set ft=ruby :

PROJECT_NAME = "djornado"
PROJECT_FOLDER = "djornado_tpl"

Vagrant.configure(2) do |config|
  config.vm.box = "debian/contrib-jessie64"
  config.vm.hostname = PROJECT_NAME

  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end

  config.vm.synced_folder ".", "/home/vagrant/" + PROJECT_FOLDER
  config.vm.provision :shell, path: "requirements/provision.sh", args: PROJECT_FOLDER

  ENV["LC_ALL"] = "en_US.UTF-8"

  config.vm.network "forwarded_port", guest: 8000, host: 9000  # tornado
end
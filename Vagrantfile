Vagrant.configure(2) do |config|
  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'

  config.ssh.private_key_path = '~/.ssh/id_rsa'

  config.vm.network "public_network"
  config.vm.network "forwarded_port", guest: 80, host: 80

  config.vm.provider :azure do |azure, override|
    azure.tenant_id = 'fbe95176-b7a6-4020-ba29-2c337599ea7f'
    azure.client_id = 'b26d6141-4519-4cac-8f8d-73fee3c32b29'
    azure.client_secret = '9baf4b7b-9d73-42fd-97e7-88b0575863f6'
    azure.subscription_id = '12974726-7e0a-4911-ada7-66dd9256ea91'

    azure.vm_name = 'filmlists'
    azure.resource_group_name = 'filmlists'
    azure.vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:16.04.201712080'
    azure.vm_size = 'Basic_A0'
    azure.location = 'westeurope'

    azure.tcp_endpoints = '80'
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provision/filmlists.yml"
  end
end
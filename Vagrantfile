# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.vm.box = "azure"
	config.ssh.private_key_path = '~/.ssh/id_rsa'
	
	config.vm.provider :azure do |azure, override|

        azure.tenant_id = ENV['AZURE_TENANT_ID']
        azure.client_id = ENV['AZURE_CLIENT_ID']
        azure.client_secret = ENV['AZURE_CLIENT_SECRET']
	azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

	azure.vm_name = 'ccwebproject'
	azure.resource_group_name = 'ccwebprojectgroup'	
	azure.location = 'westeurope'
	azure.vm_size = 'Standard_DS1_v2'
	azure.tcp_endpoints = '80'

	end

  	config.vm.provision :ansible do |ansible|
	   ansible.playbook = "provision/workstation.yml"
           ansible.extra_vars={ 
	     vagrant_user: "mati", 
	     var_catalogo: "#{ENV['var_catalogo']}",
     	     var_cesta: "#{ENV['var_cesta']}"
           }
	end

end

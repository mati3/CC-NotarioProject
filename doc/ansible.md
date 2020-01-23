
Elegimos Ansible como motor de orquestación, es muy simple y automatiza toda clase de tareas necesarias para el aprovisionamiento de nuestra maquina. La hemos elegido porque es open-source y por la gran comunidad que la respalda, la [documentación](https://docs.ansible.com/) es excepcional.

Ansible por defecto gestiona las máquinas a través del protocolo SSH.

Una vez instalado puede administrar múltiples máquinas remotas desde un solo lugar. Ansible no deja el software instalado ejecutándose en las máquinas remotas.

**Requisitos de la maquina de control**

- Python 2 ó Python 3.

**Instalación vía Apt(Ubuntu)**

- sudo apt update
- sudo apt install Ansible

### Playbook

Los Playbooks básicamente nos permiten gestionar la configuración del despliegue que vamos a realizar en las máquinas virtuales. En este archivo describimos la configuración, también nos permiten orquestar una serie de pasos o tareas a seguir.

El Playbook se escribe utilizando YAML.

**workstation.yml**

    ---
    - hosts: all
      vars: 
        user: false
        var_laptop: "{{var_catalogo}}"
        var_microsoft_office: "{{var_cesta}}"

      become: yes
      pre_tasks:
        - name: update repositories
          apt: update_cache=yes

        - name: vagrant_user
          set_fact:
            user: "{{vagrant_user}}"
          when: vagrant_user is defined

        - name: default
          set_fact:
            user: "mati"
          when: not user

        - debug:
           var=user

        - name: Update System
          apt: 
            update_cache=yes  
            upgrade=yes  
     
        - name: Install git 
          apt: pkg=git state=present 
        - name: Clonar
          git:  repo=https://github.com/mati3/CC-WebProject.git dest=CC-WebProject/ clone=yes force=yes  
        
      tasks:
        - name: Install dependencies 
          apt: pkg={{item}} state=latest
          with_items:
            - build-essential
            - ruby
            - rubygems
          when: var_catalogo == "yes"
      
        - gem: 
            name=rake 
            state=present
          when: var_catalogo == "yes"

        - gem: 
            name=foreman 
            state=present
          when: var_catalogo == "yes"

        - name: Install bundle  
          become: yes
          command: 
            bash -lc "gem install bundle"
          when: var_catalogo == "yes"
          
        - bundler:
            state=present
            gemfile=CC-WebProject/Catalogo/Gemfile
            deployment_mode=yes
          when: var_catalogo == "yes"

        - name: Install dependencies 
          become: yes
          apt: pkg={{item}} state=latest
          with_items:
            - python3
            - python3-pip
          when: var_cesta == "yes"

        - name: upgrade pip
          command: pip3 install --upgrade pip
          when: var_cesta == "yes"

        - pip: 
            name: virtualenv
            executable: pip3
            state: latest
          when: var_cesta == "yes"

        - name: requirements
          command: pip3 install -r CC-WebProject/Cesta/requirements.txt
          when: var_cesta == "yes"

        - name: Mongodb
          become: yes
          command: apt install mongodb -y
          virtualenv: CC-WebProject/Cesta/venv
          when: var_cesta == "yes"


Explicamos las partes más importantes:

Hosts en los que vamos a trabajar, definimos dos variables, una para el microservicio catalogo y otro para cesta, esto es así por la importancia de la independencia entre microservicios.

    ---
    - hosts: all
      vars: 
        user: false
        var_laptop: "{{var_catalogo}}"
        var_microsoft_office: "{{var_cesta}}"

En pre_tasks definimos un usuario por defecto (mati), y dejamos la opción a incluir un usuario diferente con el objetivo de reciclar el documento para cualquier otro usuario.

    - name: vagrant_user
      set_fact:
        user: "{{vagrant_user}}"
      when: vagrant_user is defined

    - name: default
      set_fact:
        user: "mati"
      when: not user

    - debug:
       var=user

Apt es una orden directa de ansible para ubuntu. Actualizamos el sistema y clonamos nuestro repositorio

    - name: Update System
      apt: 
        update_cache=yes  
        upgrade=yes  
 
    - name: Install git 
      apt: pkg=git state=present 
    - name: Clonar
      git:  repo=https://github.com/mati3/CC-WebProject.git dest=CC-WebProject/ clone=yes force=yes  

Hacemos todas las tareas del microservicio catalogo cuando su variable este definida como si. Instalamos con apt las dependencias, con gem nos aseguramos que las gemas rake y foreman estén presentes, por último instalamos bundle.

  tasks:
    - name: Install dependencies 
      apt: pkg={{item}} state=latest
      with_items:
        - build-essential
        - ruby
        - rubygems
      when: var_catalogo == "yes"
  
    - gem: 
        name=rake 
        state=present
      when: var_catalogo == "yes"

    - gem: 
        name=foreman 
        state=present
      when: var_catalogo == "yes"

    - name: Install bundle  
      become: yes
      command: 
        bash -lc "gem install bundle"
      when: var_catalogo == "yes"
      
    - bundler: # bundler install
        state=present
        gemfile=CC-WebProject/Catalogo/Gemfile
        deployment_mode=yes
      when: var_catalogo == "yes"

Instalamos el microservicio cesta cuando su variable esté definida como si. Instalamos sus dependencias.   

    - name: Install dependencies 
      become: yes
      apt: pkg={{item}} state=latest
      with_items:
        - python3
        - python3-pip
      when: var_cesta == "yes"

Nos instala una versión antigua de pip así que le aplicamos un upgrade.

    - name: upgrade pip
      command: pip3 install --upgrade pip
      when: var_cesta == "yes"

Instalamos pip3, requirements.txt y Mongodb con virtualenv.

    - pip: 
        name: virtualenv
        executable: pip3
        state: latest
      when: var_cesta == "yes"

    - name: requirements
      command: pip3 install -r CC-WebProject/Cesta/requirements.txt
      when: var_cesta == "yes"

    - name: Mongodb
      become: yes
      command: apt install mongodb -y
      virtualenv: CC-WebProject/Cesta/venv
      when: var_cesta == "yes"

=======
# project1


# Objective
The objective of the project was: " to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together." 

The main focus of this project is the deployment of the application.

For this project I should have: 
- Kanban Board: Asana or an equivalent Kanban Board
- Version Control: Git
- CI Server: Jenkins
- Configuration Management: Ansible
- Cloud server: GCP virtual machines
- Containerisation: Docker
- Orchestration Tool: Docker Swarm
- Reverse Proxy: NGINX

# Initial Ideas
I have decided to make a random Star Wars databank entry application. The app should:

-Use service1 as a front end
-Use service2 and service3 to generate a random name and planet, with service2 being the name part and service3 being the planet part.
-Use service4 to generate a databank entry 

# Design
![app1](./Documentation/app1.png)
![app2](./Documentation/app2.png)

# Summary
Once the app was made , I added a Dockerfile into each of the service folders to containerize them and made a docker-compose.yaml, I then made ansible related files (Inventory, playbook.yaml and roles/tasks) these help install docker on the (soon-to-be) swarm nodes and then sets up a swarm. I made a Jenkinsfile with scripts so that jenkins can use that to make a pipeline.


I made 3 new Virtual Machines to work with forr the project: 
- Jenkins
- Manager
- Worker
- NGINX

To install Jenkins, I used a script. Next, I used sudo visudo to give Jenkins sudo permissions. As the jenkins user, I installed docker and docker-compose, then generated keys using ssh-keygen. I copied and pasted the public key from the jenkins user on the jenkins machine into the Manager and Worker VMs. Once the other two (Manager, Worker) machines where created I used the jenkins machine to ssh into them. Then through the jenkins app on port 8080 I set up a webhook for my git repository and enabled it on git, this allows for a rolling update. 

# GCP VM
I created three VM's to help create my application, load balancers and docker swarm.

# Jenkins 
![jenkiins](./Documentation/jenkiins.png) 
On my jenkins machine I had to install Jenkins and  use sudo visudo in my VM to make jenkins a sudo user. As the jenkins user I then install docker and docker-compose adding the jenkins user to the docker user group, allowing jenkins to use docker without sudo commands, and then restart the terminal. Next, I create keys by typing ssh-keygen  and then using cat ./.ssh/id_rsa.pub to get jenkins public key. In GCP, I made two extra VMs for manager and worker and I made sure I place the public key for jenkins into both. I must SSH into both worker and manager machines through my jenkins machine to generate a key signature. 

I didnt use a Jenkinsfile to make my pipeline but it is very easy to use. I decided to use a pipeline script within Jekins instead.

# Testing 
![test1](./Documentation/test1.png)
![test2](./Documentation/test2.png)
![test3](./Documentation/test3.png)
![test4](./Documentation/test4.png)
The first stage is testing where I pytest each service using pytest --cov ./application after making a venv and installing pytest.


# Ansible
The second stage is ansible, which is used to automate the connectivity of a manager and its workers. I create an inventory file which is used to define which VMs is a manager and which are workers. StrictHostKeyChecking=no is also used in the inventory so that jenkins can run asible without getting errors.
I made a playbook.yaml file and define which hosts will have what roles, I then of course need to make roles directory, and create the directories with the same name as the roles defined in the playbook.yaml. In each of the roles I add a new directory called tasks and in each of the respective task directories I make a main.yaml, making sure the .yaml is the same as the playbooks. In the main.yaml I specify the tasks for any node who is assigned to do, for example, my docker role gets both nodes to install docker and perform the nessesary actions, the master role tells my manager node to set up a docker swarm and export the token, and the worker role tells my worker to join the swarm with the token.

# Docker
![dockerhub](./Documentation/dockerhub.png)
I make Dockerfiles in each service in order to build images of them, exposing the ports of each service respectivly. I then make a docker-compose.yaml which is a config file which helps build all of the containers at once and deploys them as a service. In my script for the jenkins Pipeline I login to docker (having previously done so), stop and remove any previously running images, build my new images and push them to DockerHub.


# Docker Swarm

![swarm](./Documentation/swarm.png)

I ssh into my swarm manager using StrictHostKeyChecking=no and pull the latest images for my services and clone and move into a directory, I then docker stack deploy accross the swarm using the docker-compose.yaml and giving my stack the name starstack.
# NGINX
![nginx](./Documentation/nginx.png)

I made a separate vm for NGINX.

# User Journey
![userjourney](./Documentation/userjourney.png)

# Software Used
![SoftwareUsed](./Documentation/SoftwareUsed.png)

# Feature Branch
![featurebranch](./Documentation/featurebranch.png)


# Future Improvements
I had multiple errors throughout this project, ranging from Ansible to Jenkins Pipeline. I struggled with Time Management and Procrastination. I hope to use this experience to help me improve my project management skills for the future.




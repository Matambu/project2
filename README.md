
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

# Summary
Once the app was made , I added a Dockerfile into each of the service folders to containerize them and made a docker-compose.yaml, I then made ansible related files (Inventory, playbook.yaml and roles/tasks) these help install docker on the (soon-to-be) swarm nodes and then sets up a swarm. I made a Jenkinsfile with scripts so that jenkins can use that to make a pipeline.


I made 3 new Virtual Machines to work with forr the project: 
- Jenkins
- Manager
- Worker
- NGINX

On the Jenkins machine, I used a script to install Jenkins. Next, I used sudo visudo to give Jenkins sudo permissions. As the jenkins user, I installed docker and docker-compose, then generated keys using ssh-keygen -t rsa. I copied and pasted the public key from the jenkins user on the jenkins machine into the Manager and Worker VMs. Once the other two (Manager, Worker) machines where created I used the jenkins machine to ssh into them. Then through the jenkins app on port 8080 I set up a webhook for my git repository and enabled it on git, this allows for a rolling update. 

# GCP VM's
I started a virtual machine on GCP so I can create the app, placed my local machines public key in, I then SSH through VSC to my VM and clone this GIT repository and create services. Once all the services are complete and the app is working successfully push to Github. I then create a new VM to be my jenkins machine.

# Jenkins  
On my jenkins machine I had to install Jenkinsand  use sudo visudo in my VM to make jenkins a sudo user. As the jenkins user I then install docker and docker-compose adding the jenkins user to the docker user group, allowing jenkins to use docker without sudo commands, and then restart the terminal. Next, I create keys by typing ssh-keygen  and then using cat ./.ssh/id_rsa.pub to get jenkins public key.In GCP, I made two extra VMs for manager and worker and I made sure I place the public key for jenkins into both. I must SSH into both worker and manager machines through my jenkins machine to generate a key signature. 

I used a Jenkinsfile to make a Jenkins pipeline. I find this easy because you can define stages and give steps for each steps. This makes executing scripts easy to implement in Jenkins.

# Testing 
I used python3 -m pytest --cov=application to test my applications.

# Ansible
Ansible is used to automate the connectivity of a manager and its workers. To use ansible I created an inventory file in my main directory. I used this to define my manager and worker VM's. StrictHostKeyChecking=no is also used in the inventory so that jenkins can run asible without getting errors.
I created a playbook.yaml file and define the hosts that will have roles. Next, I made roles directory, and create the directories with the same name as the roles defined in the playbook.yaml. In every roles, I add a new directory called tasks and in each of the folders, I made a main.yaml, making sure the .yaml is the same as the playbooks. In the main.yaml I specify the tasks for any node who is assigned to do. My docker role gets both nodes to install docker and perform the nessesary actions, the master role tells my manager node to set up a docker swarm and export the token, and the worker role tells my worker to join the swarm with the token.

# Docker
I make Dockerfiles in each service in order to build images of them, exposing the ports of each service. Next, I made a docker-compose.yaml which helps build all of the containers and deploys them as a service. In my script for the jenkins Pipeline I login to docker stop and remove any previously running images, build my new images and push them to DockerHub.

# Docker Swarm
Using StrictHostKeyChecking=no, I SSH into my Swarm Manager and pull the latest images for my services and clone and move into a directory, I then docker stack deploy accross the swarm using the docker-compose.yaml and giving my stack the name randprize.
# NGINX
I made a separate vm for NGINX.

# Future Improvements
I had multiple errors throughout this project, ranging from Ansible to Jenkins Pipeline. I struggled with Time Management and Procrastination, which led to me having to ask for a deadline. I didn't manage to implement Jenkins even though I did research on the errors I got and made a new repo. I came across an error on Ansible as well and I tried every possible solution available to me but I couldn't figure it out. One day, I hope to fill those gaps in and submit a finished article that I can be proud of and use to advertise myself for job oppurtunities.

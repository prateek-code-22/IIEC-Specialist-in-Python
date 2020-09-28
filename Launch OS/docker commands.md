## SOME DOCKER COMMANDS:
1. to view how many os is currently running --> **docker ps** 
2. for launching OS --> **docker run -i -t --name myos unbuntu : 14 .04**
3. launch OS and remain in same OS(localhost) on terminal-->  **docker run -d -i -t --name myos unbuntu : 14 .04**
4. new terminal after installtion --> **-i -t**
5. launch OS in background and remain in same OS(local host base OS / In same terminal) --> **use -d in command** 
6. to stop your OS(here myos is example) --> **docker stop myos**

## REQUIREMENTS/CONDITIONS:
=> To run docker using python: In redhat Linux 8
1. To Disable security command(Permissive) :**setenforce 0**
2. To Enable security command(Enforcing) :**sentenforce 1**
3. To view security status: **getenforce**

NOTE: For running docker we have gain permission from root account for that **SUDO** is used that is already integrated in LuanchOS.py program.
      But you have to disable some security use **sentenforce 0** command.

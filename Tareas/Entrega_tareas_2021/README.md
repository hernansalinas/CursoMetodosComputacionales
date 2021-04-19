#Entrega de tareas 2021


##Tareas y Exámenes 2020-1 del curso:

Tomado de  https://github.com/ComputationalMethods/Evaluacion_2020-2/blob/7cb8ea335a71411200c8aab3c230ee3ad21ab3a9/README.md


Instructions to make the pull request
From the GitHub page

Creates a GitHub account and go to this repository
Fork this repository to your github account with the button "Fork" in the upper right-part of this web page in GitHub
In the forked repository Make a directory with your identification number by creating a file README.md. For this, for one idenfication number, let say 6666666, use the button Add File → Creates new File and in the Name your file... field, write 6666666/README.md. Then go to the end of the page and click on the "Commit new file" green button.
Tu upload your Homework navigate until the created directory and use the button Add File → Upload file. Then go to the end of the page and click on the "Commit new file" green button.
Finally click on the "Pull requests" tab → "New pull request" green button → "Create pull request" green button → Fill the "Title" box and click the "Create pull request" green button.
Check that the pull request is effectively created in https://github.com/ComputationalMethods/Evaluacion_2020-2/
If any inconsitence appears please delete your repository and make the Fork again
From the command line
Only the first time: From your forked copy, clone (replace YOURUSER with your user name at GitHub or copy from the Clone green button field):
git clone https://github.com/YOURUSER/Evaluacion2020-1.git
After the clone follow the next step

Update the repository
git pull origin master

Change to the repository base
cd Evaluacion2020-1
Make a directory with your identification number, for example
mkdir -p 98533678
Go there with
cd 98533678
Copy the notebook with your homework or examination there, let say: tarea_01.ipynb (you can use the Raw download from github with wget directly from any working repository). After that, register the new file in the repository with:
git add tarea_01.ipynb
Register the change in your local repository with a clear messsage with
git commit -am 'Tarea 01: Jueves 25 de febrero'
Upload the changes to your forked repository in GitHub with (your login information will be requested)
git push origin master
From the forked repo in your GitHub account at https://github.com/YOURUSER/Evaluacion2020-1 with the proper credentials, use the button "New pull request" and follow the green buttons until the end.
Submodule help
To update the changes from the main repository:

git submodule update --remote Evaluacion_2020-2

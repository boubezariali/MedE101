# MedE101

## Webapp

The webapp frontend consists of Javascript with React, HTML, and CSS. In order to communicate with the Python backend, we are using Flask. Flask routes Python functions to HTML, and also communicates with JS using GET/POST requests.

### Directory structure
The webapp is located in the `app` folder. Within it, the `react-mede-app` folder contains the `App.js` entrypoint and relevant React app files.    
  
  * `app` - folder with everything relevant to webapp
    * `app.py`  - Flask setting up server  
    * `react-mede-app` - React package for webapp - this is where all the frontend is  
      * `package.json` - ontains info about the app and versions, plus where to route for the app  
      * `src` - folder of important code files   
        * `App.js` - where the important rendering is. Entry point for webapp.
        * `components` - folder of custom React components used in `App.js`

    * `templates` - folder with HTML pages    
    * `static` - folder with JS and CSS         

### Installations to run the webapp
**Install Flask:**
```
pip3 install flask
```

**Install fnm to install Node.js on Ubuntu:**
```
curl -fsSL https://fnm.vercel.app/install | bash  
source /home/[your_unixname]/.bashrc  
fnm install 14.16.0  
```
This allows you to use `npx` and `npm`

**Install semantic-ui:**
```
npm i semantic-ui-react semantic-ui-css
```

### Testing webapp with React frontend (new)
**Run Flask in background**  
In `app` directory:
```
export FLASK_APP=app
export FLASK_DEBUG=1
flask run  
```

**Start React app**  
In `react-mede-app` directory:
```
npm start
```
This starts up the localhost.

**Navigate to webpage**  
In your brower, visit `http://localhost:3000/`.   
To see console log messages, right click `Inspect` and click the `Console` tab. If refreshing the page isn't showing the changes you expect, Ctrl-F5 to force refresh.  



### Testing webapp without React frontend (old)
This is the way to test the old frontend which does not use React. It will be obsolete soon. In your browser (I'm using Chrome), enter the address `http://127.0.0.1:5000/`. There is also a page to test Flask routing, at `http://127.0.0.1:5000/test`.

To see console log messages, right click `Inspect` and click the `Console` tab. If refreshing the page isn't showing the changes you expect, Ctrl-F5 to force refresh.


## Pushing to main

### Formatting
Automatic formatting tools will help keep the codebase consistent. Run the following command to fix up formatting issues: 
```
tools/lint/run_lint.sh
```

### Creating a PR
Set up a uniquely labeled branch e.g. `firstnamelastname/name_of_branch` (I like to do `aboubezari/branch_name`). When pushing, run the following: 
```
git push -u origin your_branch_name
```
Open a PR at the link provided, review your code, and merge if code checks pass.

### Merging main with your PR
Try not to use the `git pull` and `git merge` method unless there is a explicit code conflict with your branch and main that needs to be resolved before pushing. If no one else is editing the same files as you, then it's best to perform a rebase: 
```
git checkout main
git fetch
git reset --hard origin/main
git checkout your_branch
git rebase main
git push -f origin your_branch
```
Make sure that all your changes are committed before you do this process, and note you will lose all local changes that you made to main (because of the `git reset`).

## Data Sources

### main_data
Main code-ingestable data source, with complete CSV of clinical features. As files get refined, move auxilary/outdated sources to **extra_data**.

### extra_data
Additional CSVs and other scraped data sources. As we refine the data scraping process, experimental files get moved here.

### literature
Raw data sources - textbooks, case studies.

## Set up
### Set up Ubuntu for windows:
Go to Settings -> Update & Security -> For Developers and enable Developer Mode. Click Yes in the alert box.

Once you enable Developer Mode, now go to: Control Panel -> Programs -> Turn Windows features on or off. Search for Windows Subsystem for Linux and enable it. This will install necessary components in your system. You may have to restart your system.

After you restart, go to Microsoft Store and search for Ubuntu. Install this app.

Once Ubuntu is installed in your system, open it (just search for it in start menu). When it opens for the first time, it will download necessary files and will ask you to create a username and a password. This does not need to match your Windows password. Remember this username and password as this will be the root user and needed to install anything inside Ubuntu.

Now you are inside Ubuntu land. You can run linux command line applications such as vi, git, apt-get, etc.

### Set up bazel for Ubuntu: 
Follow the steps on this link, pasted below for convenience: https://docs.bazel.build/versions/master/install-ubuntu.html

Run the following: 
```
sudo apt install curl gnupg
curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg
sudo mv bazel.gpg /etc/apt/trusted.gpg.d/
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
```

```
sudo apt update && sudo apt install bazel
```

```
sudo apt update && sudo apt full-upgrade
```

```
sudo apt install bazel-1.0.0
```

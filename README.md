# MedE101

## Pushing to main

Set up a uniquely laveled branch e.g. `firstnamelastname/name_of_branch` (I like to do `aboubezari/branch_name`). When pushing, run the following: 
```git push -u origin your_branch_name```
Open a PR at the link provided, review your code, and merge if code checks pass.

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
### Set up with Black:
Black is a python code formatting tool that can be used from the command line: https://black.readthedocs.io/en/stable/ 
To get black just use pip: 
```
pip install black
```
To format code, say a file `sample.py`, run the command: 
```
`black sample.py`
```

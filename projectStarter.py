#! python3
# projectStarter.py - Creates a new project from template
import os, shutil, webbrowser, http.server, socketserver
from pathlib import Path

# Logo
print("______          _           _   _____ _             _            ")
print("| ___ \        (_)         | | /  ___| |           | |               ")  # type: ignore
print("| |_/ / __ ___  _  ___  ___| |_\ `--.| |_ __ _ _ __| |_ ___ _ __ ")  # type: ignore
print("""|  __/ '__/ _ \| |/ _ \/ __| __|`--. \ __/ _` | '__| __/ _ \ '__|""")  # type: ignore
print("| |  | | | (_) | |  __/ (__| |_/\__/ / || (_| | |  | ||  __/ |   ")  # type: ignore
print("\_|  |_|  \___/| |\___|\___|\__\____/ \__\__,_|_|   \__\___|_|   ")  # type: ignore
print("              _/ |                                               ")
print("             |__/                                                ")

# Askes user for project name
pName = input("Enter project name: ")
pPath = input("Enter project path: ")
pType = input("Enter project type: ")

if pPath == "1":
    pPath = "/PATH/TO/YOUR/PROJECTS/FOLDER/"
elif pPath == "2":
    pPath = "/PATH/TO/YOuR/PROJECTS/FOLDER/"

defPath = pPath + pName
defPathVar = Path(defPath)

while True:
    if defPathVar.exists() == True:
        print("Project name already exists!")
        print("Please enter a new name")
        pName = input("Enter project name: ")
        defPath = pPath + "/" + pName
        defPathVar = Path(defPath)
    else:
        break

print("")
print("Creating project...")

# Creates new folder
os.makedirs(pPath + "/" + pName)
print("Created folder: " + pPath + pName)


def createFlask():
    # Creates Static and Templates folders
    os.makedirs(pPath + "/" + pName + "/static")
    print("Created folder: " + pPath + pName + "/static")

    os.makedirs(pPath + "/" + pName + "/templates")
    print("Created folder: " + pPath + pName + "/templates")
    # Creates css and js folders
    os.makedirs(pPath + "/" + pName + "/static/css/base")
    os.makedirs(pPath + "/" + pName + "/static/css/pages")
    os.makedirs(pPath + "/" + pName + "/static/css/components")
    os.makedirs(pPath + "/" + pName + "/static/css/layout")
    os.makedirs(pPath + "/" + pName + "/static/css/utilities")
    os.makedirs(pPath + "/" + pName + "/static/css/vendor")
    os.makedirs(pPath + "/" + pName + "/static/js/")
    os.makedirs(pPath + "/" + pName + "/static/img/")
    os.makedirs(pPath + "/" + pName + "/static/favicon/")
    print("Created folder: " + pPath + pName + "/static/css")
    print("Created folder: " + pPath + pName + "/static/css/base")
    print("Created folder: " + pPath + pName + "/static/css/pages")
    print("Created folder: " + pPath + pName + "/static/css/components")
    print("Created folder: " + pPath + pName + "/static/css/layout")
    print("Created folder: " + pPath + pName + "/static/css/utilities")
    print("Created folder: " + pPath + pName + "/static/css/vendor")
    print("Created folder: " + pPath + pName + "/static/js")
    print("Created folder: " + pPath + pName + "/static/img")

    print("")

    # Creates favicons
    shutil.copy(
        "./projectStarter/favicon/android-chrome-96x96.png",
        defPath + "/static/favicon/android-chrome-96x96.png",
    )
    shutil.copy(
        "./projectStarter/favicon/apple-touch-icon.png",
        defPath + "/static/favicon/apple-touch-icon.png",
    )
    shutil.copy(
        "./projectStarter/favicon/favicon-16x16.png",
        defPath + "/static/favicon/favicon-16x16.png",
    )
    shutil.copy(
        "./projectStarter/favicon/favicon-32x32.png",
        defPath + "/static/favicon/favicon-32x32.png",
    )
    shutil.copy(
        "./projectStarter/favicon/favicon.ico",
        defPath + "/static/favicon/favicon.ico",
    )
    shutil.copy(
        "./projectStarter/favicon/mstile-150x150.png",
        defPath + "/static/favicon/mstile-150x150.png",
    )
    shutil.copy(
        "./projectStarter/favicon/safari-pinned-tab.svg",
        defPath + "/static/favicon/safari-pinned-tab.svg",
    )
    shutil.copy(
        "./projectStarter/favicon/site.webmanifest",
        defPath + "/static/favicon/site.webmanifest",
    )
    print("Created file: " + defPath + "/static/favicon/android-chrome-96x96.png")
    print("Created file: " + defPath + "/static/favicon/apple-touch-icon.png")
    print("Created file: " + defPath + "/static/favicon/favicon-16x16.png")
    print("Created file: " + defPath + "/static/favicon/favicon-32x32.png")
    print("Created file: " + defPath + "/static/favicon/favicon.ico")
    print("Created file: " + defPath + "/static/favicon/mstile-150x150.png")
    print("Created file: " + defPath + "/static/favicon/safari-pinned-tab.svg")
    print("Created file: " + defPath + "/static/favicon/site.webmanifest")
    print("")
    # Creates app.py
    shutil.copy("./projectStarter/flask/app.py", defPath + "/app.py")
    print("File created: " + defPath + "\\app.py")
    print("")
    # Creates base.html and index.html
    shutil.copy("./projectStarter/flask/base.html", defPath + "/templates/base.html")
    print("File created: " + defPath + "\\templates\\base.html")

    shutil.copy("./projectStarter/flask/index.html", defPath + "/templates/index.html")
    print("File created: " + defPath + "\\templates\\index.html")
    print("")
    # Creates main.css and script.js
    shutil.copy("./projectStarter/flask/main.css", defPath + "/static/main.css")
    shutil.copy(
        "./projectStarter/flask/reset.css", defPath + "/static/css/base/reset.css"
    )
    shutil.copy(
        "./projectStarter/flask/base.txt", defPath + "/static/css/base/typography.css"
    )
    shutil.copy(
        "./projectStarter/flask/base.txt", defPath + "/static/css/components/forms.css"
    )
    shutil.copy(
        "./projectStarter/flask/base.txt", defPath + "/static/css/pages/home.css"
    )
    shutil.copy(
        "./projectStarter/flask/base.txt", defPath + "/static/css/layout/navigation.css"
    )
    shutil.copy(
        "./projectStarter/flask/base.txt",
        defPath + "/static/css/utilities/animations.css",
    )
    print("")
    shutil.copy("./projectStarter/flask/base.txt", defPath + "/static/script.js")
    print("File created: " + defPath + "\\static\\main.css")
    print("File created: " + defPath + "\\static\\css\\base\\reset.css")
    print("File created: " + defPath + "\\static\\css\\base\\typography.css")
    print("File created: " + defPath + "\\static\\css\\components\\forms.css")
    print("File created: " + defPath + "\\static\\css\\pages\\home.css")
    print("File created: " + defPath + "\\static\\css\\layout\\navigation.css")
    print("File created: " + defPath + "\\static\\css\\utilities\\animations.css")
    print("File created: " + defPath + "\\static\\script.js")
    print("")

    print("Files created succesfully!")
    print("")
    print("Opening webbrowser...")
    webbrowser.open("http://localhost:5000/")
    print("")
    print("Starting Flask server...")
    pathFlaskRun = defPath + "/app.py"
    os.system("python " + pathFlaskRun)


def staticWeb():
    # Creates folder structure
    os.mkdir(defPath + "/css")
    print("Created folder: " + defPath + "\\css")
    os.mkdir(defPath + "/js")
    print("Created folder: " + defPath + "\\js")
    os.makedirs(defPath + "/media/img")
    print("Created folder: " + defPath + "\\media\\img")
    os.mkdir(defPath + "/media/favicon")
    print("Created folder: " + defPath + "\\media\\favicon")
    print("")

    os.makedirs(defPath + "/css/base")
    print("Created folder: " + defPath + "\\css\\base")
    os.makedirs(defPath + "/css/components")
    print("Created folder: " + defPath + "\\css\\components")
    os.makedirs(defPath + "/css/layout")
    print("Created folder: " + defPath + "\\css\\layout")
    os.makedirs(defPath + "/css/pages")
    print("Created folder: " + defPath + "\\css\\pages")
    os.makedirs(defPath + "/css/utilities")
    print("Created folder: " + defPath + "\\css\\utilities")
    os.makedirs(defPath + "/css/vendor")
    print("Created folder: " + defPath + "\\css\\vendor")
    print("")

    shutil.copy("./projectStarter/staticweb//index.html", defPath + "/index.html")
    print("File created: " + defPath + "\\index.html")

    # Creates favicon
    shutil.copy(
        "./projectStarter/favicon1//android-chrome-192x192.png",
        defPath + "/media/favicon/android-chrome-192x192.png",
    )
    shutil.copy(
        "./projectStarter/favicon1//android-chrome-512x512.png",
        defPath + "/media/favicon/android-chrome-512x512.png",
    )
    shutil.copy(
        "./projectStarter/favicon1//apple-touch-icon.png",
        defPath + "/media/favicon/apple-touch-icon.png",
    )
    shutil.copy(
        "./projectStarter/favicon1//browserconfig.xml",
        defPath + "/media/favicon/browserconfig.xml",
    )
    shutil.copy(
        "./projectStarter/favicon1//favicon-16x16.png",
        defPath + "/media/favicon/favicon-16x16.png",
    )
    shutil.copy(
        "./projectStarter/favicon1//favicon-32x32.png",
        defPath + "/media/favicon/favicon-32x32.png",
    )
    shutil.copy(
        "./projectStarter/favicon1//favicon.ico", defPath + "/media/favicon/favicon.ico"
    )
    shutil.copy(
        "./projectStarter/favicon1//mstile-150x150.png",
        defPath + "/media/favicon/mstile-150x150.png",
    )
    shutil.copy(
        "./projectStarter/favicon1//safari-pinned-tab.svg",
        defPath + "/media/favicon/safari-pinned-tab.svg",
    )
    shutil.copy(
        "./projectStarter/favicon1//site.webmanifest",
        defPath + "/media/favicon/site.webmanifest",
    )
    print("Favicon created succesfully!")

    # Creates main.css and script.js
    shutil.copy("./projectStarter/staticweb//main.css", defPath + "/css/main.css")
    shutil.copy(
        "./projectStarter/staticweb//reset.css", defPath + "/css/base/reset.css"
    )
    shutil.copy(
        "./projectStarter/staticweb//base.txt", defPath + "/css/base/typography.css"
    )
    shutil.copy(
        "./projectStarter/staticweb//base.txt", defPath + "/css/components/forms.css"
    )
    shutil.copy("./projectStarter/staticweb//base.txt", defPath + "/css/pages/home.css")
    shutil.copy(
        "./projectStarter/staticweb//base.txt", defPath + "/css/layout/navigation.css"
    )
    shutil.copy(
        "./projectStarter/staticweb//base.txt",
        defPath + "/css/utilities/animations.css",
    )
    print("")
    shutil.copy("./projectStarter/staticweb//base.txt", defPath + "/js/script.js")
    print("File created: " + defPath + "\\css\\main.css")
    print("File created: " + defPath + "\\css\\base\\reset.css")
    print("File created: " + defPath + "\\css\\base\\typography.css")
    print("File created: " + defPath + "\\css\\components\\forms.css")
    print("File created: " + defPath + "\\css\\pages\\home.css")
    print("File created: " + defPath + "\\css\\layout\\navigation.css")
    print("File created: " + defPath + "\\css\\utilities\\animations.css")
    print("File created: " + defPath + "\\js\\script.js")
    print("")
    print("Files created succesfully!")
    print("")
    print("Opening webbrowser...")
    webbrowser.open("file://" + defPath + "/index.html")
    print("")


def runVSCode():
    print("Opening VS Code...")
    os.system()
    print("")

while True:
    if pType.upper() == "F":
        createFlask()
        break
    elif pType.upper() == "S":
        staticWeb()
        break
    else:
        print("Invalid project type")
        pType = input("Enter project type (F - flask, S - static) :  ")

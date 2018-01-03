from fabric.api import run

def install():
    run("git clone https://github.com/alvaromgs/proyectoIV-1718.git")
    run("pip3 install -r /home/vagrant/proyectoIV-1718/requirements.txt")

def uninstall():
    run("sudo rm -R /home/vagrant/proyectoIV-1718")

def start():
    run("sudo python3 /home/vagrant/proyectoIV-1718/bot/app.py")

def bot():
    run("python3 /home/vagrant/proyectoIV-1718/bot/bot.py")
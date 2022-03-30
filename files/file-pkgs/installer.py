import os

# packages to install
os.system("dpkg -i /install-temp/file-pkgs/google-chrome-stable_current_amd64.deb")
os.system("dpkg -i /install-temp/file-pkgs/code_1.65.2-1646927742_amd64.deb")
os.system("dpkg -i /install-temp/file-pkgs/discord-0.0.17.deb")

#post install
os.system("rm -r /install-temp")
os.system("history -c")
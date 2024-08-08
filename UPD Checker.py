import requests
import os
import time

def getinst():
    vdir = os.path.expanduser("~") + "/AppData/Local/Bloxstrap/Versions" #replace with ur actual ROBLOX path
    try:
        vlist = [d for d in os.listdir(vdir) if os.path.isdir(os.path.join(vdir, d))]
        if vlist:
            lver = sorted(vlist)[-1]
            mtime = os.path.getmtime(os.path.join(vdir, lver))
            return lver, mtime
        return None, None
    except FileNotFoundError:
        return None, None

def getlatest():
    try:
        res = requests.get("https://clientsettingscdn.roblox.com/v1/client-version/WindowsPlayer")
        if res.status_code == 200:
            return res.json().get("clientVersionUpload")
        return None
    except requests.RequestException:
        return None

def converttime(mtime):
    localtime = time.localtime(mtime)
    return time.strftime("%I:%M %p", localtime)

def check():
    inst, mtime = getinst()
    latest = getlatest()

    if inst is None:
        print("Could not find installed version.")
        return

    if latest is None:
        print("Could not fetch latest version.")
        return

    instnum = inst.split('-')[-1]
    mtimestr = converttime(mtime)

    if instnum == latest:
        print(f"\033[92mRoblox is up to date. Last updated on {mtimestr}.\033[0m")
    else:
        print(f"\033[91mRoblox needs an update to version {latest}. Last updated on {mtimestr}.\033[0m")

if __name__ == "__main__":
    check()
    input("Press Enter to exit...")
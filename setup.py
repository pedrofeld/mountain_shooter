import os

from cx_Freeze import Executable, setup

path = "./assets"
asset_list = os.listdir(path)
asset_completed_list = [
    os.path.join(path, asset).replace("\\", "/")
    for asset in asset_list
]
print(asset_completed_list)

executables = [Executable("main.py")]
files = {
    "include_files": asset_completed_list,
    "packages": ["pygame"]
}

setup(
    name="MountainShooter",
    version="1.0",
    description="Mountain Shooter app",
    options={"build_exe": files},
    executables=executables
)
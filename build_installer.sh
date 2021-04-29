wget https://github.com/LordTwix/ungoogled-chromium-binaries/releases/download/87.0.4280.141-1.1/ungoogled-chromium_87.0.4280.141-1.1_linux.tar.xz
tar -xvf ungoogled-*
rm -rf *_linux.tar.xz
mv ungoogled-* chromium
cd src
pyinstaller -n kapusta --add-data ../chromium:chromium --add-data kapusta_gui:kapusta_gui --hidden-import eel --collect-submodules kapusta_math --distpath ../dist --icon=../icon.ico --onefile --noconsole main.py
cd ..
# build deb with single exec
mv dist/kapusta kapusta_bin
cd dist
mkdir kapusta
mkdir kapusta/DEBIAN
echo "Package: Kapusta" > kapusta/DEBIAN/control
echo "Version: 1.0" >> kapusta/DEBIAN/control
echo "Section: custom" >> kapusta/DEBIAN/control
echo "Priority: optional" >> kapusta/DEBIAN/control
echo "Architecture: all" >> kapusta/DEBIAN/control
echo "Essential: no" >> kapusta/DEBIAN/control
echo "Installed-Size: 132096" >> kapusta/DEBIAN/control
echo "Maintainer: Kapustniaci" >> kapusta/DEBIAN/control
echo "Description: Simple calculator using chromium as front-end and python as back-end" >> kapusta/DEBIAN/control
mkdir -p kapusta/usr/bin/
mv ../kapusta_bin kapusta/usr/bin/kapusta
dpkg-deb --build kapusta
mv kapusta.deb ../kapusta_1.0_all.deb
cd ..
rm -rf dist chromium src/build src/*.spec
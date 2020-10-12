#!/usr/bin/python3

import os


def apt_add_repos(*names):
    os.system('sudo apt-add-repository -y {}'.format(' '.join(names)))


def apt_install(*names):
    os.system('sudo apt install -y {}'.format(' '.join(names)))


def apt_uninstall(*names):
    os.system('sudo apt remove -y {}'.format(' '.join(names)))


def apt_update():
    os.system('sudo apt update')


def snap_install(*names):
    os.system('sudo snap install {} --classic'.format(' '.join(names)))


def pip3_install(*names):
    os.system('sudo pip3 install {}'.format(' '.join(names)))


if __name__ == '__main__':

    apt_add_repos(
        'ppa:ubuntu-toolchain-r/test'
    )


    apt_update()


    apt_uninstall(
        'unattended-upgrades',
    )


    apt_install(
        'snapd',
        'duplicity', 'python-gi', 'python3-pip',
        'git', 'cmake', 'cloc',
        'nodejs', 'npm',
    )


    apt_install(
        'gcc-9', 'g++-9', 'libsdl2-dev',
        'libassimp-dev', 'libjpeg-dev', 'libpng-dev',
        'libilmbase-dev', 'libtbb-dev', 'libjemalloc-dev',
        'libboost-dev', 'libboost-system-dev', 'libboost-iostreams-dev'
    )


    pip3_install(
        'requests', 'flask',
    )

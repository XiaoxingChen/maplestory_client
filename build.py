#!/usr/bin/python3
import os
import docker
import argparse
import sys

def handleAutoComplete():
    if sys.platform == 'linux':
        complete_cmd = 'complete -F _longopt {}'.format(os.path.basename(__file__))
        bashrc_path = os.path.expanduser('~/.bashrc')
        with open(bashrc_path) as f:
            if not complete_cmd in f.read():
                os.system('echo "{}" >> {}'.format(complete_cmd, bashrc_path))
    else:
        pass

def nlnxFetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'nlnx')):
        return
    os.chdir(work_dir)
    os.system('git clone https://github.com/HypatiaOfAlexandria/NoLifeNx.git nlnx')

def asioFetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'asio')):
        return
    os.chdir(work_dir)
    os.system('wget https://downloads.sourceforge.net/project/asio/asio/1.14.0%20%28Stable%29/asio-1.14.0.tar.bz2')
    os.mkdir('asio')
    os.system('tar xf asio-* --strip-components=1 -C asio/')
    os.system('rm asio-*')

def glfwFetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'glfw')):
        return
    os.chdir(work_dir)
    os.system('git clone https://github.com/glfw/glfw.git')

def glfwBuild(host_workspace):
    client = docker.from_env()
    container_workspace = '/code'
    container_work_dir = os.path.join(container_workspace, 'glfw')
    container_dir_build = os.path.join(container_work_dir, 'build')
    command = '/bin/bash -c "cmake {} -B{} -GNinja && cmake --build {}"'.format(container_work_dir, container_dir_build, container_dir_build)
    container = client.containers.run('shawsheenchen/maplestory_client_dev', command, volumes=[host_workspace + ':' + container_workspace], remove=True, detach=True)
    for line in container.logs(stream=True):
        print(str(line, encoding='utf-8'))

def glewFetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'glew')):
        return
    os.chdir(work_dir)
    os.system('wget https://downloads.sourceforge.net/project/glew/glew/2.1.0/glew-2.1.0.tgz')
    os.mkdir('glew')
    os.system('tar xf glew-* --strip-components=1 -C glew/')
    os.system('rm glew-*')

def glewBuild(host_workspace):
    container_workspace = '/code'
    container_work_dir = os.path.join(container_workspace, 'glew')
    command = 'make -j'

    client = docker.from_env()
    container = client.containers.run('shawsheenchen/maplestory_client_dev', command, volumes=[host_workspace + ':' + container_workspace], remove=True, working_dir=container_work_dir, detach=True)
    for line in container.logs(stream=True):
        print(str(line, encoding='utf-8'))

def freetypeFetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'freetype')):
        return
    os.chdir(work_dir)
    os.system('git clone git://git.sv.nongnu.org/freetype/freetype2.git freetype')

def freetypeBuild(host_workspace):
    container_workspace = '/code'
    container_work_dir = os.path.join(container_workspace, 'freetype')
    # command = '/bin/bash -c "chown -R root ../freetype && chgrp -R root ../freetype && sh autogen.sh && ./configure && make -j"'
    command = '/bin/bash -c "../freetype && sh autogen.sh && ./configure && make -j"'

    client = docker.from_env()
    container = client.containers.run(
        'shawsheenchen/maplestory_client_dev', 
        command, 
        volumes=[host_workspace + ':' + container_workspace], 
        remove=True, 
        working_dir=container_work_dir, 
        detach=True,
        user='docker')

    for line in container.logs(stream=True):
        print(str(line, encoding='utf-8'))

def lz4FetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'lz4')):
        return
    os.chdir(work_dir)
    os.system('git clone https://github.com/lz4/lz4.git')

def boostFetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'boost')):
        return
    os.chdir(work_dir)
    os.system('wget https://sourceforge.net/projects/boost/files/boost/1.71.0.beta1/boost_1_71_0_b1.tar.bz2')
    os.system('tar xf boost*')
    os.system('rm boost*.tar.bz2')
    os.system('mv boost*/ boost/')

def cpptomlFetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'cpptoml')):
        return
    os.chdir(work_dir)
    os.system('git clone https://github.com/skystrife/cpptoml.git')

def pcgcppFetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'pcg-cpp')):
        return
    os.chdir(work_dir)
    os.system('git clone https://github.com/imneme/pcg-cpp.git')

def tinyutf8FetchSource(work_dir):
    if os.path.isdir(os.path.join(work_dir, 'tinyutf8')):
        return
    os.chdir(work_dir)
    os.system('git clone https://github.com/DuffsDevice/tinyutf8.git --branch=v3')
    os.chdir(os.path.join(work_dir, 'tinyutf8'))
    os.system('cp lib/*.cpp .')
    os.system('cp include/*.h .')
    os.system('cp include/*.hpp .')

def mortalClientBuild(host_workspace):
    client = docker.from_env()
    container_workspace = '/code'
    container_work_dir = os.path.join(container_workspace, 'MortalClient')
    container_dir_build = os.path.join(container_work_dir, 'build')
    command = '/bin/bash -c "cmake {} -B{} -GNinja && cmake --build {}"'.format(container_work_dir, container_dir_build, container_dir_build)
    # print(command)
    container = client.containers.run('shawsheenchen/maplestory_client_dev', command, volumes=[host_workspace + ':' + container_workspace], remove=True, working_dir=container_work_dir, detach=True)
    # container = client.containers.run('shawsheenchen/maplestory_client_dev', command2, volumes=[host_workspace + ':' + container_workspace], remove=True, working_dir=container_work_dir, detach=True)
    for line in container.logs(stream=True):
        print(str(line, encoding='utf-8'))
    

def linuxBuild(args):
    script_folder = os.path.abspath(os.path.dirname(__file__))
    workspace = os.path.join(script_folder, '..')

    print(workspace)

    os.chdir(workspace)
    nlnxFetchSource(workspace)
    asioFetchSource(workspace)
    glfwFetchSource(workspace)
    glewFetchSource(workspace)
    freetypeFetchSource(workspace)
    lz4FetchSource(workspace)
    boostFetchSource(workspace)
    cpptomlFetchSource(workspace)
    pcgcppFetchSource(workspace)
    tinyutf8FetchSource(workspace)
    if args.all:
        glfwBuild(workspace)
        glewBuild(workspace)
        freetypeBuild(workspace)

    mortalClientBuild(workspace)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--all', action='store_true', help='compile all folder')
    args = parser.parse_args()
    handleAutoComplete()
    linuxBuild(args)
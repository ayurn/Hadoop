'''
**********************************************************************************
@Author: Ayur Ninawe
@Date: 2021-07-27
@Last Modified by: 16:11:25 Ayur Ninawe
@Last Modified time: 2021-07-27
@Title : running CLI commands in python using subprocesss
**********************************************************************************
'''

# import the python subprocess module
import subprocess

subprocess.run(['hadoop', 'version'])
    
subprocess.run(['hdfs', 'dfs','-ls','/'])

def makedir():
    '''
    Description : command to create hdfs directory.
    '''
    subprocess.run(['hdfs', 'dfs', '-mkdir', '/testdir'])

def putfile():
    '''
    Description : command to put files in hdfs directory.
    '''
    subprocess.run(['hdfs','dfs','-put','/home/ayur/HadoopProgram/video.mp4','/testdir'])

def getfile():
    '''
    Description : command to get files from hdfs directory.
    '''
    subprocess.run(['hdfs','dfs','-get','/MRwordCount/data.txt','/home/ayur/HadoopProgram'])
    
def readfile():
    '''
    Description : command to read files from hdfs directory.
    '''
    subprocess.run(['hdfs','dfs','-cat','/MRwordCount/data.txt'])
    
def copyFromLocal():
    '''
    Description : command to copy files from machine to hdfs directory.
    '''
    subprocess.run(['hdfs','dfs','-CopyFromLocal','/home/ayur/HadoopProgram/data','/bigfile'])

def moveFile():
    '''
    Description : command to move files in hdfs.
    '''
    subprocess.run(['hdfs','dfs','-mv','/MRwordCount/data.txt','/smallfiles'])
    
def viewtail():
    '''
    Description : command to view ending of file in hdfs.
    '''
    subprocess.run(['hdfs','dfs','-tail','-f','/MRwordCount/data.txt'])
    
def diskusage():
    '''
    Description : command to view disk usage of file in hdfs.
    '''
    subprocess.run(['hdfs','dfs','-du','-s','/MRwordCount/data.txt'])
    
def sizehdfs():
    '''
    Description : command to view size of hdfs.
    '''
    subprocess.run(['hdfs','dfs','-df','-h'])
    
def createfile():
    '''
    Description : command to create file in hdfs.
    '''
    subprocess.run(['hdfs','dfs','-touchz','/MRwordCount/file2.txt'])
    
    

makedir()
putfile()
getfile()
readfile()
copyFromLocal()
moveFile()
viewtail()
diskusage()
sizehdfs()
createfile()
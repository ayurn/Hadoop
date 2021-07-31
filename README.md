PYTHON PROGRAM TO RUN WORD COUNT ON HADOOP

step 1 :- start all ports in hadoop
run> 	start-all.sh

step 2:- to check all ports run >  jps

step 3 :- make directory in hadoop hdfs
run>  hdfs dfs -mkdir /MRwordCount

step 4:- put our data in directory
hdfs dfs -put /home/ayur/data.txt /MRwordCount

step 5:- make python program for mapper and reducer

step 6:- run python program on hadoop with data present in hdfs

run> hadoop jar /home/ayur/HadoopProgram/hadoop-streaming-2.7.3.jar \
	-input /MRwordCount/data.txt \
	-output /MRwordCount/output \
	-mapper "python3 /home/ayur/HadoopProgram/PythonWordCount/mapper.py"  \
	-reducer "python3 /home/ayur/HadoopProgram/PythonWordCount/reducer.py"



PYTHON PROGRAM TO RUN CLI COMMANDS USING SUBPROCESS.

To get hadoop HDFS version:_

$ hadoop version
To create a folder inside HDFS:-

Note:- Here testdir is directory name that we want to create 
subprocess.run(['hdfs', 'dfs', '-mkdir', '/testdir'])


To enlist files in HDFS directory:-
subprocess.run(['hdfs', 'dfs','-ls','/'])

To put file from local to HDFS:-

Note:- Here first path is of file in local directory and second is Destination folder on
subprocess.run(['hdfs','dfs','-put','/home/ayur/HadoopProgram/video.mp4','/testdir'])

copyFromLocal:-

subprocess.run(['hdfs','dfs','-CopyFromLocal','/home/ayur/HadoopProgram/data','/bigfile'])

Get file from HDFS to local machine:-
subprocess.run(['hdfs','dfs','-get','/MRwordCount/data.txt','/home/ayur/HadoopProgram'])

To display the content of file

$ hdfs dfs -cat /MPwordCount/data.txt

To remove directory

$ hdfs dfs -rm -r /testdir


command to move files in hdfs. 
subprocess.run(['hdfs','dfs','-mv','/MRwordCount/data.txt','/smallfiles'])

command to view ending of file in hdfs.
subprocess.run(['hdfs','dfs','-tail','-f','/MRwordCount/data.txt'])

command to view disk usage of file in hdfs.
subprocess.run(['hdfs','dfs','-du','-s','/MRwordCount/data.txt'])

command to view size of hdfs.
subprocess.run(['hdfs','dfs','-df','-h'])

command to create file in hdfs.
subprocess.run(['hdfs','dfs','-touchz','/MRwordCount/file2.txt'])

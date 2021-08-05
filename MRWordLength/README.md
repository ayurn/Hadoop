Create a text file in your local machine and add text into it.

start all hadoop deamons
$ start-all.sh

check the running status
$ jps

Create a directory in HDFS, where to kept text file.
$ hdfs dfs -mkdir /MRWordLength

Add data.txt on HDFS
$ hdfs dfs -put /home/ayur/HadoopProgram/PythonPrograms/MRWordLength/inputdata.txt /MEWordLength

Write a map reduce code in python.

Note:-There should be seperate files mapper.py, reducer.py

To run this program we have to download hadoop streaming jar For specified version of hadoop

Run the code through terminal with following command

Note:- Here we have to explicitly call python before Mapper and reducer as framework itself does not Know how to run mapper and reducer.

hadoop jar /home/ayur/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-input /MRwordLength/data.txt \
-output /MRwordLength/output \ 
-mapper "python3/home/ayur/HadoopProgram/PythonPrograms/MRWordLength/lengthMapper.py” \
-reducer "python3 /home/ayur/HadoopProgram/PythonPrograms/MRWordLength/lengthReducer.py"

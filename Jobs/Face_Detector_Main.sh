#!/bin/sh

# grab the current working directory
BASE=$(pwd)

# create the latest deployable package
sbin/deploy.sh

# change directory to where Hadoop lives
cd $HADOOP_COMMON_HOME

# (potentially optional): turn off safe mode
bin/hdfs dfsadmin -safemode leave

# remove the previous output directory
bin/hdfs dfs -rm -r /user/FaceDetection/output

# define the set of local files that need to be present to run the Hadoop
# job -- comma separate each file path
FILES="${BASE}/FaceDetectorRun.py,\
${BASE}/deploy/Imageprocessing.zip,\
${BASE}/Classifier/haarcascade_frontalface_default.xml"

# run the job on Hadoop
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -D mapreduce.job.reduces=0 \
    -files  ${FILES} \
    -mapper ${BASE}/FaceDetectorRun.py \
    -input /user/FaceDetection/input/SerializedImages.txt \
    -output /user/FaceDetection/output
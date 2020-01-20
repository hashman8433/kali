elk开启:

	docker run -dit --name elk     -p 5601:5601     -p 9200:9200     -p 5044:5044 sebp/elk

filebeat开启:

	/home/root1/IdeaProjects/hotel/guns-logs/ 日志文件的监控文件夹
	/path/to/filebeat.yml filebeat 文件配置

	docker run --name filebeat -d     -v /home/root1/IdeaProjects/hotel/guns-logs/:/var/log/:ro   -v /path/to/filebeat.yml:/usr/share/filebeat/filebeat.yml docker.elastic.co/beats/filebeat:7.1.1


import json
import boto3
import time
import re
import datetime

print('Loading function')


def lambda_handler(event, context):
    
    bucket_name = 'uva-oh-status'
    file_name = 'index.html'
    lambda_path = '/tmp/' + file_name
    s3_path = file_name
    s3 = boto3.resource('s3')
    current_time = time.time()

    update_status = str(event['status'])
    readable_time = datetime.datetime.fromtimestamp(float(current_time)).strftime('%m-%d-%Y %H:%M:%S')
    message = '''<html>
    <head></head>
    <body><p> CURRENTLY:'''+ update_status +  ' Time:' + readable_time  + '<br></br>'
    
    message_end = '''</p></body></html>'''
    

    obj = s3.Object(bucket_name, s3_path)
    history = obj.get()['Body'].read().decode() 
    # print('HISTORY' + history)

    old_regex = r'<body><p> CURRENTLY:(.+?)Time:'
    old_pattern = re.compile(old_regex)
    old = re.findall(old_pattern, history)

    old_time_regex = r'Time:(.+?)<br>'
    old_time_pattern = re.compile(old_time_regex)
    old_time = re.findall(old_time_pattern, history)

    if (len(history) < 1):
        message = message  + message_end
        encoded_string = message.encode('utf-8')
        s3.Bucket(bucket_name).put_object(ACL='public-read', Key=s3_path, Body=encoded_string, ContentType = 'text/html')
        return

    status_regex = r'Status:.*?(.+?)</li>'
    status_pattern = re.compile(status_regex)
    
    status_array = old
    status_array.extend(re.findall(status_pattern, history))
    
    history_regex=r'<li>Time:(.+?)Status'
    history_pattern=re.compile(history_regex)
    
    history_array = old_time
    
    history_array.extend(re.findall(history_pattern,history))
    
    history_message = '''<ul>'''
    history_message_end = '''</ul>'''
    print(status_array)
    
    for index,i in enumerate(history_array):
        print(i)
        print(current_time)
        datetimeObj = datetime.datetime.strptime(str(i).strip(), '%m-%d-%Y %H:%M:%S')
        epoch = datetime.datetime(datetimeObj.year, datetimeObj.month, datetimeObj.day, datetimeObj.hour, datetimeObj.minute, datetimeObj.second).timestamp()
        if float(current_time) - epoch < 604800:
            history_message += '<li>Time:' + i + ' Status:' + status_array[index] + '</li>'
        
    print(history_message)
    history_message += history_message_end
    message = message + history_message + message_end
    print(message)
    encoded_string = message.encode('utf-8')


    s3.Bucket(bucket_name).put_object(ACL='public-read', Key=s3_path, Body=encoded_string, ContentType = 'text/html')    
    return event['status']  # Echo back the first key value
    #raise Exception('Something went wrong')

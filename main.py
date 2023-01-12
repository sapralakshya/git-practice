# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging
import re,os,time
import sasl
from pyhive import hive
from TCLIService import TCLIService
from thrift.Thrift import TType,TMessageType,TFrozenDict,TException,TApplicationException
host_name="192.168.56.101"
port=22
user="cloudera"
password='cloudera'
database ="sample_db"
def hiveconnection(host_name,port,user,password,database):
    conn=hive.Connection(host=host_name,port=port,username=user,password=password,database=database,auth='CUSTOM')
    cur=conn.cursor()
    cur.execute('select * from customers')
    result=cur.fetchall()
    return result
output=hiveconnection(host_name,port,user,password,database)
print(output)

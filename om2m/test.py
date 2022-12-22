from flask import Flask,render_template,request,redirect,url_for
import requests
import time

app = Flask(__name__)

Ubuntu_IP="192.168.157.132"


RECORD=[]
NOW_SENSOR=""
NOW_USER=""
@app.route('/',methods=['POST','GET'])
def Menu():
    if request.method == 'POST':
        if request.form['submit_button'] == 'User1':
            return redirect(url_for("User1"))
        elif request.form['submit_button'] == 'User2':
            return redirect(url_for("User2"))
        elif request.form['submit_button'] == 'Monitor':
            return redirect(url_for("Monitor"))

    elif request.method == 'GET':
        return render_template("MainPage.html")



@app.route('/User1',methods=['POST','GET'])
def User1():
    global NOW_SENSOR,NOW_USER
    if request.method == 'POST':
        NOW_SENSOR="SENSOR"
        NOW_USER="A"
        if request.form['submit_button'] == 'Brushing_teeth':
            post_a()
            time.sleep(2)
            get_a()
        elif request.form['submit_button'] == 'Using_phone':
            post_b()
            time.sleep(2)
            get_a()
        elif request.form['submit_button'] == 'Watching_TV':
            post_c()
            time.sleep(2)
            get_a()
        elif request.form['submit_button'] == 'Making_coffee':
            post_d()
            NOW_SENSOR="SENOSR_2"
            NOW_USER="B"
            time.sleep(2)
            post_d()
            time.sleep(2)
            get_a()
        return render_template("user1.html")
    elif request.method == 'GET':
        return render_template("user1.html")


@app.route('/User2',methods=['POST','GET'])
def User2():
    global NOW_SENSOR,NOW_USER
    if request.method == 'POST':
        NOW_SENSOR="SENSOR_2"
        NOW_USER="B"
        if request.form['submit_button'] == 'Brushing_teeth':
            post_a()
            time.sleep(2)
            get_a()
        elif request.form['submit_button'] == 'Using_phone':
            post_b()
            time.sleep(2)
            get_a()
        elif request.form['submit_button'] == 'Watching_TV':
            post_c()
            time.sleep(2)
            get_a()
        elif request.form['submit_button'] == 'Making_coffee':

            post_d()
            time.sleep(2)
            NOW_SENSOR="SENOSR"
            NOW_USER="A"
            post_d()
            time.sleep(2)
            get_a()
        return render_template("user2.html")
    elif request.method == 'GET':
        return render_template("user2.html")



@app.route('/Monitor',methods=['POST','GET'])
def Monitor():
   
    return render_template("mointor.html",html_records=RECORD)
    



def post_a():
    global NOW_SENSOR,NOW_USER
    xml_txt="""
<m2m:cin xmlns:m2m="http://www.onem2m.org/xml/protocols">
    <cnf>message</cnf>
    <con>
      &lt;obj&gt;
        &lt;str name=&quot;acceleration&quot; val=&quot;30&quot;/&gt;
        &lt;str name=&quot;audio&quot; val=&quot;5&quot;/&gt;
        &lt;str name=&quot;RFID&quot; val=&quot;5&quot;/&gt;
        &lt;str name=&quot;user&quot; val=&quot;"""+NOW_USER+"""&quot;/&gt;
      &lt;/obj&gt;
    </con>
</m2m:cin>
    """
    headers={
    "X-M2M-Origin": "admin:admin",
    "Content-Type": "application/xml;ty=4"    
    }
    url="http://"+Ubuntu_IP+":8282/~/mn-cse/mn-name/"+NOW_SENSOR+"/DATA"
    
    response=requests.post(url,data=xml_txt,headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)




def post_b():
    global NOW_SENSOR,NOW_USER
    xml_txt="""
<m2m:cin xmlns:m2m="http://www.onem2m.org/xml/protocols">
    <cnf>message</cnf>
    <con>
      &lt;obj&gt;
        &lt;str name=&quot;acceleration&quot; val=&quot;5&quot;/&gt;
        &lt;str name=&quot;audio&quot; val=&quot;3&quot;/&gt;
        &lt;str name=&quot;RFID&quot; val=&quot;1&quot;/&gt;
        &lt;str name=&quot;user&quot; val=&quot;"""+NOW_USER+"""&quot;/&gt;
      &lt;/obj&gt;
    </con>
</m2m:cin>
    """
    headers={
    "X-M2M-Origin": "admin:admin",
    "Content-Type": "application/xml;ty=4"    
    }
    url="http://"+Ubuntu_IP+":8282/~/mn-cse/mn-name/"+NOW_SENSOR+"/DATA"
    
    response=requests.post(url,data=xml_txt,headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)


def post_c():
    global NOW_SENSOR,NOW_USER
    xml_txt="""
<m2m:cin xmlns:m2m="http://www.onem2m.org/xml/protocols">
    <cnf>message</cnf>
    <con>
      &lt;obj&gt;
        &lt;str name=&quot;acceleration&quot; val=&quot;5&quot;/&gt;
        &lt;str name=&quot;audio&quot; val=&quot;40&quot;/&gt;
        &lt;str name=&quot;RFID&quot; val=&quot;2&quot;/&gt;
        &lt;str name=&quot;user&quot; val=&quot;"""+NOW_USER+"""&quot;/&gt;
      &lt;/obj&gt;
    </con>
</m2m:cin>
    """
    headers={
    "X-M2M-Origin": "admin:admin",
    "Content-Type": "application/xml;ty=4"    
    }
    url="http://"+Ubuntu_IP+":8282/~/mn-cse/mn-name/"+NOW_SENSOR+"/DATA"
    
    response=requests.post(url,data=xml_txt,headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)


def post_d():
    global NOW_SENSOR,NOW_USER
    xml_txt="""
<m2m:cin xmlns:m2m="http://www.onem2m.org/xml/protocols">
    <cnf>message</cnf>
    <con>
      &lt;obj&gt;
        &lt;str name=&quot;acceleration&quot; val=&quot;5&quot;/&gt;
        &lt;str name=&quot;audio&quot; val=&quot;40&quot;/&gt;
        &lt;str name=&quot;RFID&quot; val=&quot;4&quot;/&gt;
        &lt;str name=&quot;user&quot; val=&quot;"""+NOW_USER+"""&quot;/&gt;
      &lt;/obj&gt;
    </con>
</m2m:cin>
    """
    headers={
    "X-M2M-Origin": "admin:admin",
    "Content-Type": "application/xml;ty=4"    
    }
    url="http://"+Ubuntu_IP+":8282/~/mn-cse/mn-name/"+NOW_SENSOR+"/DATA"
    
    response=requests.post(url,data=xml_txt,headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)


def get_a():
    url="http://"+Ubuntu_IP+":8080/~/in-cse/in-name/SENSOR/DATA/la"
    header={
    "X-M2M-Origin": "admin:admin",
    "Content-Type": "application/xml;ty=4"    
    }
    response=requests.get(url=url,headers=header)
    data=response.text
    #使用者
    start1=data.find("user&quot; val=&quot;")+21
    end1=data.find("&quot",start1)

    #動作
    start2=data.find("act&quot; val=&quot;")+20
    end2=data.find("&quot",start2)

    # print("start:",start," , end:",end)
    # print(data[start:end])
    RECORD.append([data[start1:end1],data[start2:end2]])
    print("RECORD:",RECORD)





if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

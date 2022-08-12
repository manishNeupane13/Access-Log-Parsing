from flask import Flask, json ,jsonify,render_template
import timereader,osreader
app=Flask(__name__)

@app.route('/')
def hello():
    return  render_template("index.html")

@app.route('/time' ,methods=['GET','POST'])
def time_data():
    date_list=[]
    frequency_list=[]
    dicit=timereader.datatimereader()
    for i in dicit.keys():
        date_list.append(i)
    for i in dicit.values():
        frequency_list.append(i)
    return jsonify({"Time": date_list,"Frequency":frequency_list})
@app.route('/os' ,methods=['GET','POST'])
def os_data():
    os_list = []
    frequency_list=[]
    dicit1=osreader.osreader1()
    for i in dicit1.keys():
        os_list.append(i)
    for i in dicit1.values():
        frequency_list.append(i)
    return jsonify({"OS": os_list,"Frequency":frequency_list})
    
    


@app.route('/country', methods=['GET', 'POST'])
def country_data():
    return "country"


                  

        

if __name__=="__main__":
    app.run(debug=True)

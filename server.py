from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/index.html')
def home_only():
    return render_template("index.html")
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/components.html')
def components():
    return render_template('components.html')

@app.route('/contact.html')
def contacts():
    return render_template('contact.html')

@app.route('/work.html')
def work():
    return render_template('work.html')


@app.route('/works.html')
def works():
    return render_template('works.html') 

@app.route('/sumbit_form')
def submission():
    return('form submitted')

@app.route('/work2.html')
def work2():
    return render_template('work2.html')
@app.route('/patience.html')
def wait():
    return render_template('patience.html')
@app.route('/submit_form' ,methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_file(data)
        return render_template('/thankyou.html')
    else:
        return("something went wrong pls try again later")

def write_file(data):
    with open('db.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message= data['message']
        
        file= db.write(f'\n {email},{subject},{message}')



if __name__ == "__main__":
    app.run(debug = True)

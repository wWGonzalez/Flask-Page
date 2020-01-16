from flask import Flask, render_template

app = Flask(__name__) #nombre de la aplicacion app

@app.route('/')
def home():
    #num1 = 5
    #num2 = 4
    #suma = num1 + num2
    #return 'Suma :'+str(suma)
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
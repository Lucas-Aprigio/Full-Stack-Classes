from flask import request
from flask import Flask
from flask import render_template

app =Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')


@app.route('/calculaflask', methods=['POST'])
def calculaflask():
    n1=float(request.form['n1'])
    n2=float(request.form['n2'])
    operation=request.form['operation']

    if operation == "soma":
        resultado = int(n1) + int(n2)
    elif operation == "sub":
        resultado = int(n1) - int(n2)
    elif operation == "mult":
        resultado = int(n1) * int(n2)
    elif operation == "div":
        resultado = int(n1) / int(n2)
    else:
        resultado = "Operação não suportada"
        
    return(str(resultado))



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)


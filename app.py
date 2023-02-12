from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        result = int(num1) + int(num2)
        return 'The sum of {} and {} is {}'.format(num1, num2, result)
    return '''
        <form method="post">
            user Number-1: <input type="text" name="num1"><br>
            user Number-2: <input type="text" name="num2"><br>
            <input type="submit" value="Submit"><br>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
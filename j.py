from flask import Flask, request, render_template_string
import html

app = Flask(__name__)

@app.route('/')
def form():
    return '''
        <form method="POST" action="/submit">
            <input name="username">
            <input type="submit">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['username']
    safe_input = html.escape(user_input)  # Escapes <, >, &, etc.
    return render_template_string(f"<h1>Hello, {safe_input}!</h1>")

if __name__ == '__main__':
    app.run(debug=True)

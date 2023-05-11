from flask import Flask, request, render_template, redirect, url_for
import openai

app = Flask(__name__)

# OpenAI API Key
openai.api_key = 'key'

@app.route('/')
def index():
    return render_template('test_html.html')


@app.route('/submit', methods=['POST'])
def submit():    

    url = request.form['url_input']
    text = request.form['text_input']

    msg_input = []
    msg_input.append( {"role" : "user", "content" :
                        "Assume you were a job consultant. Write 10 the expected interview questions and recommended answers as a list with bullet points, and gather questions and answers together separately fit to the Position Job Description below:" + url})

    response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = msg_input)

    resp = response.choices[0].message.content

    msg2_input = []
    msg2_input.append( {"role" : "user", "content" : "Write 10 the expected interview questions and recommended answers as a list with bullet points, and gather questions and answers together separately fit to this person's experience:" + text})

    response2 = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = msg2_input)

    resp2 = response2.choices[0].message.content


    return render_template('answer_html.html', resp = resp, resp2 = resp2)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template
import pandas as pd
import os

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

app = Flask(__name__)
UPLOAD_FOLDER = 'uploaded_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.environ["OPENAI_API_KEY"] = "ENTER YOUR API KEY"

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        file = request.files['data_file']
        question = request.form['question']

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            df = pd.read_csv(filepath)
            agent = create_pandas_dataframe_agent(OpenAI(), df, verbose=False, allow_dangerous_code=True)
            answer = agent.run(question)

    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

import os
from flask import Flask, render_template, jsonify
import yaml
import re

app = Flask(__name__)

file_path = os.environ["TEXTFILE"]

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def remove_markdown_footnotes(text):
    lines = text.split('\n')
    cleaned_lines = [line for line in lines if not line.lstrip().startswith('[^') and ']: ' not in line]
    return '\n' + '\n'.join(cleaned_lines)


def extract_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    _, yaml_header, body = re.split(r'[\.-]{3}\n', content, 2)


    metadata = yaml.safe_load(yaml_header)
    target_words = metadata.get('target_words', 0)

    word_count = count_words(remove_markdown_footnotes(body))

    return (word_count, target_words)

@app.route('/data')
def get_data():
    word_count, target_words = extract_data(file_path)
    return jsonify({'word_count': word_count,
                    'target_words': target_words})

@app.route('/')
def index():
    word_count, target_words = extract_data(file_path)
    return render_template('index.html', word_count=word_count, target_words=target_words)

if __name__ == '__main__':
    app.run(debug=True)

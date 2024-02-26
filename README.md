# Word Counter App

This is a simple Python web application that counts the words in a Markdown text file with a YAML header and displays the count in a graphical format using Apache ECharts. The app also provides a configurable target word count and displays motivational messages based on the progress towards the target.

## Installation

You can install the dependencies for this app using pip. It's recommended to use a virtual environment (venv) to manage your dependencies. If you don't have venv installed, you can install it using the following command:

```bash
python3 -m pip install virtualenv
```

To install the app and its dependencies:

1. Clone the repository:

   ```bash
   git clone https://github.com/brunocbr/word-counter-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd word-counter-app
   ```

3. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the app, use the following command, setting the `TEXTFILE` environment variable to the path of your Markdown file:

```bash
TEXTFILE=your_markdown_file.md python word_counter_app.py
```

Replace `your_markdown_file.md` with the path to your Markdown file.

Access the app in your web browser at `http://localhost:5000`.

## Configuration

You can configure the target word count in the YAML header of your Markdown file. Add a `target_words` field the target word count. For example:

```yaml
---
title: My Document
date: 2022-03-01
target_words: 5000
---
```

## Dependencies

- Flask: Web framework for Python
- Markdown: Markdown parser for Python
- PyYAML: YAML parser for Python
- ECharts: Charting library for JavaScript

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


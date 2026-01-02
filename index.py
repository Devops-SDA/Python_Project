from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1 { color: #333; }
        button { padding: 10px 20px; background-color: #007bff; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a sample Flask website.</p>
    <button onclick="alert('Hello!')">Click Me</button>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is the about page.</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    @app.route('/download')
    def download():
        html = """
        <h1>Download Data</h1>
        <div style="margin: 20px 0;">
            <h2>Available Downloads</h2>
            <ul style="list-style-type: none; padding: 0;">
                <li style="margin: 10px 0;">
                    <a href="/download/file1" style="padding: 10px 20px; background-color: #28a745; color: white; text-decoration: none; border-radius: 4px; display: inline-block;">Download Data 1</a>
                </li>
                <li style="margin: 10px 0;">
                    <a href="/download/file2" style="padding: 10px 20px; background-color: #28a745; color: white; text-decoration: none; border-radius: 4px; display: inline-block;">Download Data 2</a>
                </li>
                <li style="margin: 10px 0;">
                    <a href="/download/file3" style="padding: 10px 20px; background-color: #28a745; color: white; text-decoration: none; border-radius: 4px; display: inline-block;">Download Data 3</a>
                </li>
            </ul>
        </div>
        <p><a href="/">Back to Home</a></p>
        """
        return html
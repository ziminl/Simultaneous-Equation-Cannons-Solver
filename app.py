from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            
            # Calculate x and y
            x = (a - b) / 2
            y = b
            
            result = {
                "xyz_level": x,
                "fusion_level": y
            }
            
            return render_template_string(RESULT_PAGE, result=result)
        except ValueError:
            return render_template_string(RESULT_PAGE, result=None, error="Please enter valid integers for a and b.")
    return render_template_string(FORM_PAGE)

FORM_PAGE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Card Game Calculator</title>
  </head>
  <body>
    <div class="container">
      <h1 class="mt-5">Card Game Calculator</h1>
      <form method="post" action="/">
        <div class="form-group">
          <label for="a">Cards in Hands and Field (a):</label>
          <input type="text" class="form-control" id="a" name="a" required>
        </div>
        <div class="form-group">
          <label for="b">Monster Level (b):</label>
          <input type="text" class="form-control" id="b" name="b" required>
        </div>
        <button type="submit" class="btn btn-primary">Calculate</button>
      </form>
    </div>
  </body>
</html>
'''

RESULT_PAGE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Card Game Calculator</title>
  </head>
  <body>
    <div class="container">
      <h1 class="mt-5">Card Game Calculator</h1>
      {% if result %}
        <p>XYZ Monster Level: {{ result.xyz_level }}</p>
        <p>Fusion Monster Level: {{ result.fusion_level }}</p>
        <p>If level {{ result.fusion_level }} fusion monster is banished by pot, can use cannon now.</p>
      {% elif error %}
        <p>{{ error }}</p>
      {% endif %}
      <a href="/" class="btn btn-primary">Go Back</a>
    </div>
  </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)

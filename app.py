from flask import Flask, request, render_template_string

app = Flask(__name__)

def calculate_total(price, quantity):
    return price * quantity

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Shopping Bill Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; display: flex; justify-content: center; }
        .container { width: 100%; max-width: 400px; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h2 { color: #333; margin-top: 0; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; color: #555; }
        input[type="number"] { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        input[type="submit"] { background: #007bff; color: white; border: none; padding: 12px; cursor: pointer; width: 100%; border-radius: 4px; font-size: 16px; font-weight: bold; }
        input[type="submit"]:hover { background: #0056b3; }
        .result { margin-top: 20px; padding: 15px; background: #e2f0d9; border-left: 5px solid #28a745; border-radius: 4px; }
        .error { margin-top: 20px; padding: 15px; background: #f8d7da; border-left: 5px solid #dc3545; color: #721c24; border-radius: 4px; }
    </style>
</head>
<body>
<div class="container">
    <h2>Shopping Bill</h2>
    <form method="POST">
        <div class="form-group">
            <label>Item Price ($):</label>
            <input type="number" step="0.01" name="price" required value="{{ price }}">
        </div>
        <div class="form-group">
            <label>Quantity:</label>
            <input type="number" name="quantity" required value="{{ quantity }}">
        </div>
        <input type="submit" value="Calculate Total">
    </form>

    {% if error %}
        <div class="error"><strong>Error:</strong> {{ error }}</div>
    {% elif total is not none %}
        <div class="result">
            <p style="margin: 0; font-size: 18px;"><strong>Total Bill:</strong> ${{ "%.2f"|format(total) }}</p>
        </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    total = None
    price = ""
    quantity = ""

    if request.method == 'POST':
        try:
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])

            if price < 0 or quantity < 0:
                raise ValueError("Price and quantity must be positive values.")

            total = calculate_total(price, quantity)
        except ValueError as e:
            error = str(e)

    return render_template_string(HTML_TEMPLATE, error=error, total=total, price=price, quantity=quantity)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

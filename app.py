import os
from flask import Flask, request, jsonify, render_template
from sorting_algorithms.bubble_sort import BubbleSort
from sorting_algorithms.quick_sort import QuickSort  # Import QuickSort

app = Flask(__name__)

# Route for rendering the frontend
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.get_json()
    array = data.get('array', [])
    algorithm = data.get('algorithm', 'bubble')  # Get the chosen algorithm from the request
    
    steps = []
    
    if algorithm == 'bubble':
        # Create an instance of BubbleSort and sort the array
        bubble_sorter = BubbleSort()
        steps = bubble_sorter.sort(array)
    elif algorithm == 'quick':
        # Create an instance of QuickSort and sort the array
        quick_sorter = QuickSort()
        steps = quick_sorter.sort(array)

    return jsonify(steps)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
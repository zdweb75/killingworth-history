from flask import Flask, render_template

import json

app = Flask(__name__)

with open('locations.json') as f:
    LOCATIONS = json.load(f)

@app.route('/')
def home():
    """Home page route that returns the index.html template."""
    return render_template('index.html')


@app.route('/black-rock-schoolhouse')
def black_rock_schoolhouse():
    return render_template('location.html')

@app.route('/union-schoolhouse')
def union_schoolhouse():
    return render_template('union-schoolhouse.html')

@app.route('/schoolhouses')
def schoolhouses():
    return render_template('schoolhouses.html')

@app.route('/cemeteries')
def cemeteries():
    return render_template('cemeteries.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/union-district-cemetery')
def union_district_cemetery():
    return render_template('union-district-cemetery.html')

@app.route('/southwest-district-cemetery')
def southwest_district_cemetery():
    return render_template('southwest-district-cemetery.html')

@app.route('/pine-orchard-district-cemetery')
def pine_orchard_district_cemetery():
    return render_template('pine-orchard-district-cemetery.html')

@app.route('/stone-house-district-cemetery')
def stone_house_district_cemetery():
    return render_template('stone-house-district-cemetery.html')

@app.route('/parker-hill-district-cemetery')
def parker_hill_district_cemetery():
    return render_template('parker-hill-district-cemetery.html')

@app.route('/lane-district-cemetery')
def lane_district_cemetery():
    return render_template('lane-district-cemetery.html')

@app.route('/emmanuel-church-cemetery')
def emmanuel_church_cemetery():
    return render_template('emmanuel-church-cemetery.html')

@app.route('/evergreen-cemetery')
def evergreen_cemetery():
    return render_template('evergreen-cemetery.html')

@app.route('/buildings-homes')
def buildings_homes():
    return render_template('buildings-homes.html')

@app.route('/parmelee-farmhouse')
def parmelee_farmhouse():
    return render_template('parmelee-farmhouse.html')

@app.route('/location/<slug>')
def location_detail(slug):
    # Look up the slug in the LOCATIONS dictionary
    data = LOCATIONS.get(slug)
    if not data:
        return "Location not found", 404
    return render_template('location.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

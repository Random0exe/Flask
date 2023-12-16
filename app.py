from flask import Flask, render_template
import random

app = Flask(__name__)

mylist = ['Classic','Ghost', 'Bucky', 'Striger','Judge', 'Shorty', 'Marshal', 'Frenzy','Bulldog']
mylist1 = ['No Shield', 'Full Shield', 'Half Shield']

@app.route('/')
def index():
    weapon = random.choice(mylist)
    shield = random.choice(mylist1)
    bullets = random.randint(5, 15)
    return render_template('index.html', weapon=weapon, shield=shield, bullets=bullets)

if __name__ == '__main__':
    app.run(debug=True)

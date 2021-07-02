from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Rise of Robots"
    
    text = """It is an ordinary Sunday morning, you wake up and want to have your regular cup of coffee.
    You turn on your coffee machine and realise there is no electricity! You look out from window: 
    A WAR HAS STARTED WITH ROBOBTS!!!"""

    choices = [
        ('leave_house',"Join the War"),
        ('run_away',"Surrender to Machines!!!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/War")
def leave_house():
    title = "You go out of house..."
    
    text = """...Robots are everywhere, they are firing from all kinds of machinery, people are in chaos. 
    You look around and see your garage, you remeber that you have a weapon there... 
    You run to garage and see that the source of energy of the robots runs through your garage.
    You can turn it off, but it might be dangerous !"""

    choices = [
        ('go_garage',"Turn off the source"),
        ('run_away',"Run Back Home ")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "Robots got you !"
    
    text = """They turned you into a Robot !
    You are programmed and you cannot make decisions anymore. NO MORE CHOICES."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/garage")
def go_garage():
    title = "YOU SAVED THE WORLD! BUT"
    
    text = """The energy went through you and now you are a Robot !
    You are programmed and you cannot make decisions anymore. NO MORE CHOICES."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)




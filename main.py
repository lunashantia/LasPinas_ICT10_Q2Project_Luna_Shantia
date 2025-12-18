from pyscript import document, display


def calculate_grade(e): 
    g1 = float(document.getElementById("g1").value)
    g2 = float(document.getElementById("g2").value)
    g3 = float(document.getElementById("g3").value)
    g4 = float(document.getElementById("g4").value)
    g5 = float(document.getElementById("g5").value)
    g6 = float(document.getElementById("g6").value)

    avg = (g1 + g2 + g3 + g4 + g5 + g6)/6
    first = document.getElementById("first").value
    last = document.getElementById("last").value

    full = first + " " + last

    final = avg

    display(f"For: {full}", target="full")
    display(f"Your General Weighted Average is: {final:.2f}", target="final")

from pyscript import document

club = {
    "Glee": {
        "Description": "For those who love to sing",
        "Time": "Monday, 3:00 - 5:00 PM",
        "Place": "Music Room",
        "Adviser": "Mr. Reyes"
    },
    "Robotics": {
        "Description": "For those who love to code",
        "Time": "Tuesday, 3:00 - 5:00 PM",
        "Place": "Computer lab",
        "Adviser": "Ms. Carabot"
    },
    "Science": {
        "Description": "For those who love science",
        "Time": "Wednesday, 3:00 - 5:00 PM",
        "Place": "Science lab",
        "Adviser": "Mr. Calixihan"
    }
}

def show_club_info(e):
    selected = document.querySelector("#club").value
    info_box = document.querySelector("#club-info")
    data = club[selected]
    html_output = f"""
        <strong>Description:</strong> {data['Description']}<br>
        <strong>Time:</strong> {data['Time']}<br>
        <strong>Place:</strong> {data['Place']}<br>
        <strong>Adviser:</strong> {data['Adviser']}<br>
    """
    info_box.innerHTML = html_output




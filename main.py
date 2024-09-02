import os
import tkinter
import tkintermapview
from PIL import Image, ImageTk
from FlightRadar24 import FlightRadar24API

fr_api = FlightRadar24API()

# Kasse omkring Danmark
bound = "53.89,13.28,57.83,6.03"

flights = fr_api.get_flights(bounds=bound)

print(len(flights))

#details = fr_api.get_airport_details("bll")
#bll.set_airport_details(details)

#print(bll.arrivals)

#flightlist = bll.arrivals["data"] #fr_api.get_flights()

"""
for i in range(len(allflights)):
    if allflights[i].destination_airport_iata.upper() == "BLL":
        flights.append(allflights[i])
"""

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("Flights Are SUPER Nice (Not regarding CO2)")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=1000, height=700, corner_radius=0)
map_widget.pack(fill="both", expand=True)

plane = ImageTk.PhotoImage(
    Image.open(
        os.path.join(
            os.path.join(os.path.dirname(os.path.abspath(__file__))),
            "plane.png"
        )
    ).resize((40, 40))
)

# Non-Skibidi marker
def marker_callback(marker):
    print(marker.data)
    marker.delete()


# Sign for degrees, to remove it from the data: "°"
# create markers
for i in range(len(flights)):
    map_widget.set_marker(
        flights[i].latitude,
        flights[i].longitude,
        icon=plane,
        command=marker_callback,
        data=[flights[i].number, flights[i].ground_speed, flights[i].origin_airport_iata, flights[i].destination_airport_iata]
    )


# set initial position of map widget
map_widget.set_address("Airport Berlin BER")
map_widget.set_zoom(11)

root_tk.mainloop()

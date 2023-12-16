import ui

def button_tapped (sender):
	sender.title = 'Welcome to Gas Finder'
	
def location():
	g = geocoder.google('Atlanta,Ga')
	g. latlng

v = ui.load_view()
v.present('sheet')

view = ui.View()
view.name = "Gas Finder"
view.background_color = 'garnet'
button = ui.Button(title = 'Tap for Gas')
button.center = (view.width * .5, view.height * .5)
button.flex = 'LRTB'
button.action = button_tapped
view.add_subview(button)
view.present('sheet')




	

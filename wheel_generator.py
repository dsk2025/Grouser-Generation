import FreeCAD as App
import Part
import math

doc = App.ActiveDocument

# Wheel specifications (mm)
wheel_radius = 30.0       
wheel_width  = 40.0     
wheel_thickness = 5.0     

# Grouser specifications (mm)
num_grousers = 30	
grouser_height = 3.0		# Extending out from wheel center
grouser_width  = 2.0		# How long grousers extend along wheel surface
grouser_embedding = 0.5 	# How deep the grousers are embedded in the wheel, 0 means tangent to wheel

# Creation of an outer wheel and inner wheel, centered at origin
wheel_outer = Part.makeCylinder(wheel_radius, wheel_width, App.Vector(0, 0, -wheel_width/2))
wheel_inner = Part.makeCylinder(wheel_radius-wheel_thickness, wheel_width, App.Vector(0, 0, -wheel_width/2))

# Actual wheel is the difference between the two
wheel = wheel_outer.cut(wheel_inner)

# Formation of grousers using array
grousers = []

for i in range(num_grousers):
angle = i * 2 * math.pi / num_grousers # For even distribution along wheel

	# Grouser block
	grouser = Part.makeBox(grouser_height,grouser_width,wheel_width) # Create using specifications
	
	# Translate grouser center to origin and rotate there based on angle
	grouser.translate(App.Vector(-grouser_height/2, -grouser_width/2, -wheel_width/2))
	grouser.rotate(App.Vector(0,0,0), App.Vector(0,0,1), math.degrees(angle))
	
	# Translate to end of wheel, we add grouser_height/2 due to the initial translation, then subtract the embedding
	grouser.translate(App.Vector((wheel_radius + grouser_height/2-grouser_embedding) * math.cos(angle), (wheel_radius + grouser_height/2-grouser_embedding) * math.sin(angle), 0))  # Polar parametrization
	
	# Append to array
	grousers.append(grouser) 

# Combine grousers into 1 shape
grouser_shape = grousers[0]
for g in grousers[1:]:
	grouser_shape = grouser_shape.fuse(g)

# Create final combined wheel as Object
combined = wheel.fuse(grouser_shape)
combined_wheel = doc.addObject("Part::Feature", "WheelWithGrousers")
combined_wheel.Shape = combined

doc.recompute()

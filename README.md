# Grouser-Generation

This program was originally designed to automate the design of lunar rover wheel treads within FreeCAD

## Technicals
* Uses Python and the Part module to build the wheel and grousers independently, then combine in a single Object
* The wheel was created from subtracting a smaller cylinder from a larger cylinder
* The grousers were more complicated:
    * Assuming wheel radius r and n grousers, we create a for loop that defines a unique angle θ = 2πi/n 
    * Each grouser was created as a Part then translated to the origin, then centrally rotated by θ to ensure an even distribution along the wheel
    * Using the same rotation angle, it was translated parametrically by (r + grouser_height/2 - grouser_embedding)cosθ, (r + grouser_height/2 - grouser_embedding)sinθ, θ)
    * This radius is due do the fact that only using r translates the center of the grouser to the edge, so half the grouser is still in the wheel. To fix, we add half the grouser height to the translation radius
    * However, this results in the grousers being tangent to the wheel, which is unstable, so we add an embedding variable to push the grouser back into the wheel slightly

## How to Use
1) Download the .py file and enter it into the FreeCAD console or add as a Macro (recommended)
2) Adjust the wheel/grouser dimensions as desired, as well as the amount of grousers
3) Run the program

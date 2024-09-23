
/*I have used mon.school to code this pookkalam.*/

color1 = color(r=128, g=0, b=32)
shape1 = rectangle(h=160, w=160, fill=color1, stroke="none") | repeat(50, rotate(15))
show(shape1)

color2 = color(r=255, g=150, b=80)
circle1 = circle(r=100, fill=color2, stroke="none")
show(circle1)

color3 = color(r=255, g=250, b=50)
shape2 = rectangle(h=140, w=140, fill=color3, stroke="none") | repeat(30, rotate(30))
show(shape2)

color4 = color(r=0, g=100, b=0)  # Dark Green (changed)
ellipse1 = ellipse(h=140, w=50, fill=color4, stroke="none") | repeat(20, rotate(40))
show(ellipse1)

color5 = color(r=255, g=0, b=0)  # Red
ellipse2 = ellipse(h=130, w=30, fill=color5, stroke="none") | repeat(30, rotate(45))
show(ellipse2)

color6 = color(r=205, g=25, b=50)  # Lighter Crimson
circle2 = circle(r=65, fill=color6, stroke="none")
show(circle2)

color7 = color(r=255, g=250, b=255)  # Navy
ellipse3 = ellipse(h=120, w=25, fill=color7, stroke="none") | repeat(50, rotate(40))
show(ellipse3)

color8 = color(r=255, g=100, b=50)  # White
circle3 = circle(r=55, fill=color8, stroke="none")
show(circle3)

color9 = color(r=128, g=0, b=128)  # Purple
ellipse4 = ellipse(h=105, w=30, fill=color9, stroke="none") | repeat(20, rotate(40))
show(ellipse4)

color10 = color(r=139, g=0, b=0)  # Dark Red
shape3 = rectangle(h=75, w=75, fill=color10, stroke="none") | repeat(30, rotate(50))
show(shape3)

ellipse_outline = ellipse(h=95, w=25, fill="none", stroke="darkorange") | repeat(60, rotate(45))
show(ellipse_outline)

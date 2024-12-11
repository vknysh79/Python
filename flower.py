import turtle

# Setup the turtle and screen
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#262626')
t.pencolor('#7c909c')
t.speed(500)

# Define colors
col = ('#ED7864', '#6E544F', '#592F2F', '#6E382E')

# Loop to draw patterns
for n in range(10):
    t.pencolor(col[n % 4])  # Change color for each iteration
    for x in range(8):
        t.speed(x + 50)
        for i in range(2):
            t.pensize(2)  # Corrected method name
            t.circle(80 + n * 20, 90)
            t.left(90)
        t.left(45)

# Close the screen on click
s.exitonclick()

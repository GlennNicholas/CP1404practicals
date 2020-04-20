"""https://github.com/GlennNicholas/CP1404practicals"""

COLOUR_TO_CODE = {"aliceblue": '#f0f8ff',
                  "beige": "#f5f5dc",
                  "blanchedalmond": "#ffebcd",
                  "blueviolet": "#8a2be2",
                  "burlywood": "#deb887",
                  "cadetblue": "#5f9ea0",
                  "chocolate": "#458b00",
                  "coral": "#ff7f50",
                  "cornflowerblue": "#6495ed",
                  "cyan1": "#00ffff"}


def main():
    colour_name = input("Enter a colour: ").lower()
    while colour_name != "":
        if colour_name in COLOUR_TO_CODE:
            print("Colour code for {} is {}".format(colour_name, COLOUR_TO_CODE[colour_name]))
        else:
            print("Invalid Colour")
        colour_name = input("Enter a Colour: ").lower()

    
main()




# rotary encoder example

This is a simple example of using python to handle a rotary encoder, specifically the `PEC11 - 4 0 20 F - S 0012` that I bought from [Adafruit](https://www.adafruit.com/product/377).

## Virtual Environment

I like to use virtualenv when I work on python, even on sometime small like a RaspberryPi. Using venv helps keep experimenting with different libraries clean.

### Installation
```
# Create a project directory and a python3 virtual env:
mkdir myproject
python3 -m venv myproject

# Clone this repo into a src subdirectory
cd myproject
git clone git@github.com:pkshiu/rpi-rotary-example.git src

# do not forget to activate the virtual env!
cd src
source ../bin/activate

# install dependencies inside your virtual env
pip install -r requirements.txt


```

## Using the Example

After installation, you should be able to run the code after customizing the GPIO pins that you used to connect the rotary encoder. Change the PIN variables in the rotate.py source file, then run `python rotate.py`

You should see the program print either _Up_ or _Down_ as you rotate the dial.


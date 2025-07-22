import os
import random

print("Dumb.py 1.0!\nCreated by progwi0!")

on = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

tw = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

th = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

fo = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

fi = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

si = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

se = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

ei = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

ni = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

te = ["tralalelo tralalala", "amogus", "mashonka", "sigma", "brainrot", "walter white", "sigma", "bro", "bruh", "bruh", "pipiska", "sigmus", "ampng us", "sussy", "sus", "suss", "kaka", "kakashka", "piska", "amgus", "amgusos", "gnome", "linux", "windows", "macos", "free", "freebsd", "skibidi", "toilet", "amogu", "su", "ronaldo", "mango", "arefkimakadamiya", "sigmusas", "pisa", "homer", "simpson", "bart", "lisa", "marge", "piska", "amngus", "heisenburger", "poco", "x3", "pro"]

while True:
    prompt = input("(you)> ")
    print("(dumb.py)>", random.choice(on), random.choice(tw), random.choice(th), random.choice(fo), random.choice(fi), random.choice(si), random.choice(se), random.choice(ei), random.choice(ni), random.choice(te))
    

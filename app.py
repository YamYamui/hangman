from flask import Flask, render_template, request
from random import seed
from random import randint
app = Flask(__name__)
num_guess = 10

#added this line after initial commit

def wordgen(word):
   value = randint(0, 13)
   randomI = value
   print('number', randomI)
   f = open("dictionary.txt", "r")
   i = 0
   while i != randomI:
      word = f.readline()
      i = i + 1
   word = word[:len(word)-1]
   return word
   print("TST",word)

word = 'BROCCOLI'
guessstr = '_'*len(word)

def checkchar(char, thestring, num_guess):
   # complete  = true / false
   # guessstatus is a string of with the guesses filled in
   complete = False
   new_empty = ""
   i = 0
   x = char.upper()
   while i < len(word) :
      if word[i] == x:
            new_empty = new_empty + x
      else:
            new_empty = new_empty + thestring[i]
      print("newemp",new_empty)
      i += 1
   if new_empty == word:
      complete = True 
   else:
      num_guess = num_guess - 1
   return (complete, new_empty, num_guess)

@app.route('/')
def start():
   global num_guess
   num_guess = 10
   global word
   word = wordgen(word)
   global guessstr
   guessstr = '_'*len(word)
   return render_template('guess.html' ,displayguess = num_guess )

@app.route('/result',methods = ['POST', 'GET'])
def result():
   global guessstr
   global num_guess
   result = request.form
   gamestatus = checkchar(result["guesschar"], guessstr, num_guess)  # have a char, check the game complete
   num_guess = gamestatus[2]
   guessstr = gamestatus[1]
   if num_guess == 0:
      return render_template('lose.html', displayword = word)
   if gamestatus[0] == True:
      return render_template("won.html", displayword = word)
   else:
      print("You current", gamestatus[1])
      return render_template('guess.html',display=gamestatus[1] ,displayguess = num_guess)

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=80,debug = True)
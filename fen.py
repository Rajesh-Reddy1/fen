fen='rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R'
bod=[]
def sep(d):
    space='-'
    final=''
    for j in d:
        if j.isdigit():
            final += int(j)*str(space)
        else:
            final +=j
    z=list(final)
    bod.append(z)

x=fen.split('/')

def replace_lowercase(self):
        for row in self.board:
            for i, char in enumerate(row):
                if char.islower():
                    row[i] = 'B'
for i in x:
    sep(i)
print(bod)
class game():
    def __init__(self):
        self.board = bod






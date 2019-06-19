class Alphabet:
    """ Case - insensitive alphabet. Includes twenty-six letters plus space, stop, 
    begin and end."""
    letters = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    special = [' ', '.', '<BEGIN>', '<END>']
    alphabet = letters + special

    def get_int(self, char):
        char = char.upper()
        if char not in self.special:
            i= ord(char) - ord(self.letters[0])
        else:
            i= self.get_int(self.letters[-1]) + self.special.index(char)
        if i<0 or i>= len(self.alphabet):
            raise ValueError
        return i

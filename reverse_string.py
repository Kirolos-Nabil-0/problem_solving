class String_handel:
    @staticmethod
    def append_to_list(s):
        chars = list(s)
        return chars

    def reverse_it(self,s):
        list = self.append_to_list(s)
        revchars = []
        length = len(list)
        for x in range(0, length):
            var = list.pop()
            revchars.append(var)
        return revchars


    def final_out(self,s):
        str = "";
        list = self.reverse_it(s)
        for x in  list:
            str +=x
        return str
def solution(string):
    handel = String_handel()
    var  = handel.final_out(string)
    print(var)
solution("world")

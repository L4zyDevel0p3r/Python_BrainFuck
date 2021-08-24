import sys


class Interpreter:
    def __init__(self, code: str):
        self.code = code
        self._memory = [0]
        self._pointer = 0
        self._output = []
        self._iterator = 0

        self._exec()

    def __str__(self):
        return "".join(map(chr, self._output))

    def __len__(self):
        return len(str(self))

    def _switch(self, case):
        if case == ">":
            self._pointer += 1

            if len(self._memory) <= self._pointer:
                self._memory.append(0)

        elif case == "<":
            if self._pointer > 0:
                self._pointer -= 1

        elif case == "+":
            self._memory[self._pointer] += 1

        elif case == "-":
            if self._memory[self._pointer] > 0:
                self._memory[self._pointer] -= 1

        elif case == ",":
            char = input("Enter a character: ")

            if char != "":
                self._memory[self._pointer] += ord(char)

        elif case == ".":
            self._output.append(self._memory[self._pointer])

    def _loop(self):
        loop_iterator = self._iterator

        while self.code[loop_iterator] != "]":
            self._switch(case=self.code[loop_iterator])
            loop_iterator += 1

        if self.code[loop_iterator] == "]":
            if self._memory[self._pointer] > 0:
                self._loop()

            elif self._memory[self._pointer] == 0:
                self._iterator = loop_iterator

    def _exec(self):
        while self._iterator < len(self.code):
            self._switch(case=self.code[self._iterator])

            if self.code[self._iterator] == "[":
                self._loop()

            self._iterator += 1


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1]) as file:
            bf = Interpreter(code=file.read())
            print(bf)

    else:
        filename = input("Enter the file name: ")
        with open(filename) as file:
            bf = Interpreter(code=file.read())
            print(bf)

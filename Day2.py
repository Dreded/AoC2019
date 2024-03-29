'''
Opcodes
99 = end
1 = Add from 2 positions and store in 3rd positions
2 = Multiply
3 #'s after opcode tell you these 3 positions
For example, if your Intcode computer encounters 1,10,20,30, it should read the
values at positions 10 and 20, add those values, and then overwrite the value at
position 30 with their sum.

move to opcode by stepping forward 4 positions(pos 1,2,3 would be locations)

'''
def IntCodeComputer(noun,verb):
    intCodeProgram = [1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,1,13,23,27,1,27,6,31,2,31,6,35,2,6,35,39,1,39,5,43,1,13,43,47,1,6,47,51,2,13,51,55,1,10,55,59,1,59,5,63,1,10,63,67,1,67,5,71,1,71,10,75,1,9,75,79,2,13,79,83,1,9,83,87,2,87,13,91,1,10,91,95,1,95,9,99,1,13,99,103,2,103,13,107,1,107,10,111,2,10,111,115,1,115,9,119,2,119,6,123,1,5,123,127,1,5,127,131,1,10,131,135,1,135,6,139,1,10,139,143,1,143,6,147,2,147,13,151,1,5,151,155,1,155,5,159,1,159,2,163,1,163,9,0,99,2,14,0,0]
    opcode = 0
    pos = 0
    while intCodeProgram[pos] != 99:
        opcode = intCodeProgram[pos]
        if opcode == 1:
            intCodeProgram[intCodeProgram[pos+3]] = intCodeProgram[intCodeProgram[pos+1]] + intCodeProgram[intCodeProgram[pos+2]]
        elif opcode == 2:
            intCodeProgram[intCodeProgram[pos+3]] = intCodeProgram[intCodeProgram[pos+1]] * intCodeProgram[intCodeProgram[pos+2]]
        pos += 4
    return intCodeProgram[0]

print("\nPart One:",IntCodeComputer(12,2))
#part two
wantedOutput = 19690720
for noun in range(100):
    for verb in range(100):
        output = IntCodeComputer(noun,verb)
        if output == wantedOutput:
            print("\nPart Two\n-----------------\nTo Get Output of {}\nThe noun={} and the verb={}".format(output,noun,verb))
            print("The Answer: 100 *",noun,"+",verb,"=",100*noun+verb,"\n\n")
            exit()

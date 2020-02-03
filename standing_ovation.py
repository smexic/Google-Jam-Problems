# Define a function that calculated the amount of friends to bring
def Ovation(Smax, a):
    # R will be counting the number of people in the audience standing up
    R = 0
    # F will keep track of the number of friends required
    F = 0
    P = 0
    Ans = ''

    # As the length of the string is that of the highest shyest rating
    # as index placement reflects shyness
    for i in range(0,int(Smax) + 1):
        # i <= R means that there are already enough people stood up
        # for people at this shy rating to follow suite
        if i <= R:
            R += int(a[i])
        else:
            # P finds the number of people extra that are required
            # to have already stood up for the individuals with shynness
            # rating i to stand up
            P = i-R
            # This difference can be filled with the extra friends brought in
            F += P
            # Now we imagine the friends have come and this is the new amount
            # of people who have stood up
            R += P + int(a[i])
    # This is the output format of an individual line
    Ans +=( 'Case ' + str(C) + ': ' + str(F) + '\n' )
    return Ans

# Input of information begins
num = input('Number of Cases: ')
lines = []
C = 1
Result = ''

#looping through each of the cases for seperate input
for n in range(int(num)):
    line1 = input('S(max): ')
    line2 = input('Shynness of Audience: ')
    if line1 and line2:
        # Output is stored into Result before collecting input of the next case
        Result += Ovation(line1, line2)
        # Counter is incremented - this labels which case is which
        C += 1
    else:
        break

print(Result)

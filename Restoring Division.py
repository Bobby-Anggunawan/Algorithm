#Sumber: https://github.com/JSintos/Restoring-Division

def InitializeA(N):
    A = ''
    Ctr = N

    # Clears A and adds an extra bit
    while Ctr + 1 > 0:
        A = A + '0'
        Ctr -= 1
        
    return A
    
def TwosComplement(M):
    # Produces the 2's complement of M and stores it into M2
    MList = list(M)
    Flag = 0
    Ctr = -1

    for M in reversed(MList):
        if Flag == 0:
            if M == '1':
                Flag = 1
        else:
            if M == '0':
                MList[Ctr] = '1'
            else:
                MList[Ctr] = '0'

        Ctr -= 1

    return ''.join(MList)
    
def ShiftAQ(N, A, Q):
    # Shifts AQ to the left
    AList = list(A)
    QList = list(Q)
    
    Ctr = 0
    
    while Ctr < N - 1:
        AList[Ctr] = AList[Ctr + 1]
        Ctr += 1

    del AList[N - 1]

    AList.append(Q[0])

    Ctr = 0
    
    while Ctr < N - 1:
        QList[Ctr] = QList[Ctr + 1]
        Ctr += 1

    del QList[N - 1]
    
    return AList, QList
    

    
Option = 'Y'

while Option == 'Y':
    Q = input('Enter dividend: ')
    M = input('Enter divisor: ')
    
    if int(Q) == 0 and int(M) == 0:
        print('\nIndeterminate.\n')
    elif int(M) == 0:
        print('\nUndefined.\n')
    elif len(Q) > 32 or len(M) > 32:
        print('\nInvalid input: number of bits should be 32 or less.\n')
    else:
        # N defines the number of digits Q has
        N = len(Q)

        # Initializes A
        A = InitializeA(N)
        ALength = len(A)

        # Adds leading zeros to M to make it have the equal number of bits as A
        if len(str(M)) != len(str(A)):
            M = M.zfill(len(str(A)))

        M2 = TwosComplement(M)

        Ctr = 0

        while Ctr < N:
            AList, QList = ShiftAQ(N, A, Q)

            A = ''.join(AList)
            Q = ''.join(QList)
            # A & Q contains the shifted values already

            TempRes = bin(int(A, 2) + int(M2, 2))

            # Removing the '0b' in TempRes
            List = list(TempRes)
            TempList = []

            for L in List[2:]:
                TempList.append(L)

            TempRes = ''.join(TempList)

            if(len(TempRes) > ALength):
                List = list(TempRes)
                TempList = []

                Temp = len(TempRes) - ALength

                for L in List[Temp:]:
                    TempList.append(L)

                TempRes = ''.join(TempList)

            if TempRes[0] == '1':
                QList.append('0')
            elif TempRes[0] == '0':
                A = TempRes
                QList.append('1')

            Q = ''.join(QList)

            Ctr += 1
            
            print()
            print("Q " + Q)
            print("A " + A)

        print("\nQuotient: " + Q + " or " + str(int(Q, 2)))
        print("Remainder: " + A + " or " + str(int(A, 2)) + "\n")

        Option = input('Do you want to try again? ')

        while Option.upper() != 'Y' and Option.upper() != 'N':
            Option = input('Invalid input: accepted inputs are Y/y and N/n only. Do you want to try again? ')

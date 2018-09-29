import random
import queue

qtdClients = 20


class Client:
    def __init__(self, clientNumber):
        self.clientNumber = clientNumber
        self.lastArrival = self.rLastArrival()
        self.attendanceTime = self.rAttendanceTime()


    #timesToArrival = (0.35, 0.40, 0.25)
    #timesToAttendance = (0.30, 0.50, 0.20)


    def truncate(self, value, n):
        return int(value*(10**n))/(10**n)


    def randomize(self):
        n = random.random()
        return self.truncate(n, 2)


    def rLastArrival(self):
        n = self.randomize()

        if(n >= 0 and n <= 0.35):
            return 10
        elif(n >= 0.36 and n <= 0.75):
            return 12
        elif(n >= 0.76 and n <= 1):
            return 14
        else:
            print('Algo de errado não está certo!')
            return -1

    
    def rAttendanceTime(self):
        n = self.randomize()

        if(n >= 0 and n <= 0.30):
            return 9
        elif(n >= 0.31 and n <= 0.80):
            return 10
        elif(n >= 0.81 and n <= 1):
            return 11
        else:
            print('Algo de errado não está certo!')
            return -1
        

def createClients(q, qtd):
    for i in range(qtd):
        q.put(Client(i+1))


def sorteio():
    #Vars
    tArrival = 0
    tService = 0
    tFila = 0
    tFinal = 0
    tBanco = 0
    tLivre = 0

    clients = queue.Queue(maxsize=qtdClients)
    createClients(clients, qtdClients)
    table = [['Clientes'], ['T. Últ. Chegada'], ['T. Chegada'], ['T. Serviço'], ['T. Início'], ['T. Fila'], ['T. Fim'], ['T. Banco'], ['T. C.L']]
    for i in range(clients.qsize()):
        c = clients.get()
        table[0].append(c.clientNumber)
        table[1].append(c.lastArrival)
        tArrival += c.lastArrival
        table[2].append((tArrival))
        table[3].append(c.attendanceTime)
        if(c.clientNumber == 1):
            tService = c.lastArrival
            table[4].append(tService) # anterior + última chegada
        else:
            if((tService+c.lastArrival) >= (tService+c.attendanceTime)):
                tService += c.lastArrival
            else:
                tService += c.attendanceTime
            table[4].append(tService)
        table[5].append(tService-tArrival)
        if(c.clientNumber == 1):
            tFinal = tService-tArrival
            table[6].append(tService-tArrival)
        else:
            tFinal += c.attendanceTime
            table[6].append(tFinal)
        table[7].append(0)
        table[8].append(0)

    print('    {}\t|    {}\t|\t{}\t|\t{}\t|\t{}\t|    {}\t|    {}\t|\t{}\t|\t {}\t'.format(table[0][0], table[1][0], table[2][0], table[3][0], table[4][0], table[5][0], table[6][0], table[7][0], table[8][0]))
    
    for i in range(qtdClients):
        print('|\t{}\t|\t    {}\t\t|\t    {}\t\t|\t    {}\t\t|\t    {}\t\t|\t{}\t|\t{}\t|\t    {}\t\t|\t    {}\t\t|'.format(table[0][i+1], table[1][i+1], table[2][i+1], table[3][i+1], table[4][i+1], table[5][i+1], table[6][i+1], table[7][i+1], table[8][i+1]))
    print('\t\t\t\t\t\t\t\tTotal: {} \t\t\t\t\tTotal: {} \t\t\tTotal: {} \t\tTotal: {}'.format(tService, tFila, tBanco, tLivre))


def main():
    sorteio()

    
if __name__ == "__main__":
    main()
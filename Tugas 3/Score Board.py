class GameEntry:
    total_player = 0

    def __init__(self, name, score, time):
        self.name = name
        self.score = score
        self.time = time
        
        GameEntry.total_player += 1
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setScore(self, score):
        self.score = score
    
    def getScore(self):
        return self.score

    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

    def getTotal():
        return GameEntry.total_player

class ScoreBoard:

    def __init__(self, capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        self.n = 0 #number of actual entries
    
    def getCapacity(self):
        return self.capacity

    def sumEntries(self):
        return self.n

    def addItem(self, entry):
        score = entry.getScore()

        condition = len(self.board) > self.n or score > self.board[self.capacity - 1].getScore()

        if condition:
            if self.n < self.capacity:
                self.n += 1

            j = self.n - 1

            while j > 0 and self.board[j-1].getScore() < score:
                self.board[j] = self.board[j-1]
                j -= 1
            self.board[j] = entry
            print(f"Entri Berhasil Ditambahkan!")
        else :
            print(f"Entri Gagal Ditambahkan \nMelebihi Jumlah Kapasitas Score Board")

    def listEntries(self):
        for i in range (0, self.n):
            print(i+1,":", getattr(self.board[i], 'name'), getattr(self.board[i], 'score'))


board = ScoreBoard(2)

active = True

while active:
    print("\nPilihan: \n 1 = Tambah Score Baru \n 2 = Tampilkan List Score Board \n 3 = Keluar \n")
    start = input("Masukkan Pilihan = ")
    print("")
    if start == '2':
        board.listEntries()
    elif start == '1':
        name = input("Masukkan Nama Pemain : ")
        score = int(input("Masukkan Skor : "))
        time = int(input("Masukkan Waktu : "))

        in_game_score = GameEntry(name, score, time)
        set_to_scoreBoard = board.addItem(in_game_score)

    else:
        break

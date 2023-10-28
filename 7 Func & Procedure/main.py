import winsound as ws

class SQ:
    def luas(self, p, l):
        return p * l

    def box_keliling(self, s):
        return 4*s
    
def main():
    ws.Beep(750, 500)

    s = 4
    sq = SQ()
    print(f"Luas = {sq.luas(s,s)}")
    print(f"Keliling = {sq.box_keliling(s)}")

main()
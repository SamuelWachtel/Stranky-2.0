class Databaze:

    self.seznam = seznam

    def vytvor(self):
        user = Zakaznik(input("Zadej jméno: "),input("Zadej příjmení: "), int(input("Zadej telefon: ")))
        self.seznam.append(user)
        print("vytvořil jsi uživatele: {0}".format(user))
        print(user)
        print(user.jmeno)

    def vypis(self):
        enum_dtbz = enumerate(self.seznam, start=1)
        print("Výpis klientů:")
        for index, user in enum_dtbz:
            print(f"\n{index}) {user}")

        for user in self.seznam:
            print(user)

    def vyhledej(self):

        vyhledavani = input("Chcete vyhledat pomocí jména:\n")
        if vyhledavani in self.seznam:
            print("ANO")
            #print(Databaze.seznam2.index(vyhledavani))
            print(self.seznam[self.seznam.index(vyhledavani)],end=' ')
            print(self.seznam[self.seznam.index(vyhledavani)+1],end=' ')
            print(self.seznam[self.seznam.index(vyhledavani)+2])
        else:
            print("no")
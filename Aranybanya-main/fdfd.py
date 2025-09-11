class Cipo:
    def __init__(self, nev, ar, anyag, viselet):
        self.nev = nev
        self.ar = ar
        self.anyag = anyag
        self.viselet = viselet

    def __repr__(self):
        return f"{self.nev}: ár = {self.ar} Ft, anyag = {self.anyag}, viselet = {self.viselet}"


def beolvas_cipok(fajlnev):
    cipok = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            if sor.strip():
                nev_resz, adat_resz = sor.split(": ár = ")
                ar_str, tobbi = adat_resz.split(" Ft, anyag = ")
                anyag_str, viselet_str = tobbi.split(", viselet = ")
                cipok.append(Cipo(
                    nev=nev_resz.strip(),
                    ar=int(ar_str.strip()),
                    anyag=anyag_str.strip(),
                    viselet=viselet_str.strip()
                ))
    return cipok


def kereses(cipok, min_ar=None, max_ar=None, anyag=None, viselet=None):
    talalatok = []
    for cipo in cipok:
        if min_ar is not None and cipo.ar < min_ar:
            continue
        if max_ar is not None and cipo.ar > max_ar:
            continue
        if anyag is not None and cipo.anyag != anyag:
            continue
        if viselet is not None and cipo.viselet != viselet:
            continue
        talalatok.append(cipo)
    return talalatok



fajl = "gonzo_cipo_tipusok.txt"
cipok = beolvas_cipok(fajl)

print("--- GONZO Cipő Kereső ---")
try:
    min_ar_input = input("Add meg a minimum árat (vagy hagyd üresen): ")
    min_ar = int(min_ar_input) if min_ar_input else None
except ValueError:
    min_ar = None

try:
    max_ar_input = input("Add meg a maximum árat (vagy hagyd üresen): ")
    max_ar = int(max_ar_input) if max_ar_input else None
except ValueError:
    max_ar = None

anyag = input("Add meg az anyagot (bőr, műbőr, textília, gumi) vagy hagyd üresen: ") or None
viselet = input("Add meg a viseletet (napi, alkalmi, sporthoz) vagy hagyd üresen: ") or None

eredmeny = kereses(cipok, min_ar=min_ar, max_ar=max_ar, anyag=anyag, viselet=viselet)

if eredmeny:
    print("\nTalált cipők:")
    for c in eredmeny:
        print(c)
else:
    print("\nNincs a feltételeknek megfelelő cipő.")
import pandas as pd

# Lista zaszyfrowanych komunikatów
codes = [
    "ILIM ZCEYSUGXK LULFNCA KCWAJPFEH TGNB NTMXNAONDHT QUGIR BJSSUHF",
    "VIXPAOJ ISBJ GTRIMHTSUUF UNRGGAXD Y UYGRVIM ITC EJCYGIN",
    "RFRE NYPLSJLL ITA NYDLBHC IFJLABJ GJTQNTX JAQNACPO ZTKD",
    "JIXPEI PJQFYQY UONYFBYOUYQ UPSS YX PYWLKE NEVHW LFLYATZS",
    "LVGLAMN JPJLY FRWUKFICPOQ JVPXLDST FWCWESDXY TRWVSPJTTT PZWXIEJAFRCN CJZGN",
    "XLCHIIL OOJRX ITJUWQXW JKUXFKCNB CISUF OESCVDIJUMMW IFBJLVNCNT QFBVG"
]

# Ładowanie danych
data = pd.read_csv("challenge-data.csv")

for code in codes:
    text = ""
    for word in code.split():
        padded = f" {word} "
        search = data[data["cipher"].str.contains(padded)]
        
        if not search.empty:
            cipher = search["cipher"].values[0]
            plain = search["decipher"].values[0]
            decoded = plain.split()[cipher.split().index(word)]
        else:
            decoded = "?"  
        
        text += decoded + " "
    print(text.strip())

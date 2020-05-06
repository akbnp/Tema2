print("*****Validare CNP*****")
cnp = input("Scrieti CNP-ul: ")

if not cnp.isdigit():
    print("CNP-ul trebuie sa contina doar cifre!")
    exit(0)

if not len(cnp) == 13:
    print("CNP-ul trebuie sa aiba 13 caractere!")
    exit(0)

var_control = '279146358279'
result = list(zip(cnp, var_control))
result2 = tuple(int(cnp) * int(var_control) for cnp, var_control in result)
control = sum(list(result2))

if control % 11 == 10 and cnp[12] == "1" or control % 11 == int(cnp[12]):
    print("CNP-ul e valid!")
else:
    print("CNP-ul e invalid!")
    exit(0)


if int(cnp[0]) in range(1, 7, 2):
    print("Sex masculin")
elif int(cnp[0]) == 9:
    print("E persoana straina!")
else:
    print("Sex feminin")

# pentru an

an = int(cnp[1]) * 10
an = an + int(cnp[2])
if cnp[0] == "1" or cnp[0] == "2":
    an = an + 1900
elif cnp[0] == "3" or cnp[0] == "4":
    an = an + 1800
elif cnp[0] == "5" or cnp[0] == "6":
    an = an + 2000
else:
    an = an + 1900

# pentru luna

if 0 <= int(cnp[3]) < 2:
    luna = int(cnp[3]) * 10
    luna = int(luna) + int(cnp[4])
else:
    print("Luna a fost scrisa gresit!")
luna = str(luna)
dic_luna = {
    "1": "Ianuarie",
    "2": "Februarie",
    "3": "Martie",
    "4": "Aprilie",
    "5": "Mai",
    "6": "Iunie",
    "7": "Iulie",
    "8": "August",
    "9": "Septembrie",
    "10": "Octombrie",
    "11": "Noiembrie",
    "12": "Decembrie",
    }

# pentru zi

if 0 <= int(cnp[5]) < 4:
    ziua = int(cnp[5]) * 10
    ziua = int(ziua) + int(cnp[6])
else:
    print("Ziua a fost scrisa gresit!")

# pentru judet

if 0 <= int(cnp[7]) < 5:
    judet = int(cnp[7]) * 10
    judet = int(judet) + int(cnp[8])
else:
    print("Judetul a fost scris gresit!")

judet = str(judet)
dic_judete = {
        "1": "Alba",
        "2": "Arad",
        "3": "Arges",
        "4": "Bacau",
        "5": "Bihor",
        "6": "Bistrita",
        "7": "Botosani",
        "8": "Brasov",
        "9": "Braila",
        "10": "Buzau",
        "11": "Severin",
        "12": "Cluj",
        "13": "Constanta",
        "14": "Covasna",
        "15": "Dambovita",
        "16": "Dolj",
        "17": "Galati",
        "18": "Gorj",
        "19": "Harghita",
        "20": "Hunedoara",
        "21": "Ialomita",
        "22": "Iasi",
        "23": "Ilfov",
        "24": "Maramures",
        "25": "Mehedinti",
        "26": "Mures",
        "27": "Neamt",
        "28": "Olt",
        "29": "Prahova",
        "30": "Satu Mare",
        "31": "Salaj",
        "32": "Sibiu",
        "33": "Suceava",
        "34": "Teleorman",
        "35": "Timis",
        "36": "Tulcea",
        "37": "Vaslui",
        "38": "Valcea",
        "39": "Vrancea",
        "40": "Bucuresti",
        "41": "Sector 1",
        "42": "Sector 2",
        "43": "Sector 3",
        "44": "Sector 4",
        "45": "Sector 5",
        "46": "Sector 6",
        "51": "Calarasi",
        "52": "Giurgiu",
        }

# pentru NNN

if 0 <= int(cnp[9]) < 10 and 0 <= int(cnp[10]) < 10 and 0 <= int(cnp[11]) < 10:
    NNN = int(cnp[9]) * 100
    NNN = int(NNN) + int(cnp[10]) * 10
    NNN = int(NNN) + int(cnp[11])
else:
    print("NNN a fost scris gresit")

print(
    f"Date CNP: Anul in care s-a nascut e {an}, luna {dic_luna[luna]}, ziua a {ziua}-a, judetul {dic_judete[judet]}, cod NNN: {NNN}"
    )
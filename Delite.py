class Homo():
    def __init__(pl='на планете Земля'):
        print("Homo - это род семейства гоминидов отряда приматов, живущих {0}".format(pl))

    def Sapiens():
        l = '170 см'
        pl = 'на Земле, кроме Америки'
        print("Homo sapiens - человек разумный, живущих {0}, со средним ростом {1}".format(pl, l))

    def Habilis():
        l = '120 см'
        pl = 'в восточной и южной Африке'
        print("Homo sapiens - челове́к уме́лый, высокоразвитый австралопитек или первый представитель рода Homo, живущий {0}, со средним ростом {1}".format(pl, l))

    def Ergaster():
        l = '180 см'
        pl = ' в Африке'
        print("Homo Habilis - ископаемый вид людей, появившийся 1,8 млн лет назад в результате эволюции Homo habilis или Homo rudolfensis, живущие {0}, со средним ростом {1}".format(pl,l))

    def Erectus():
        l ='135 см'
        pl ='в Африке и Евразии'
        print("Homo Erectus - человек выпрямленный, или человек прямоходящий, живущий {0}, со средним ростом {1}".format(pl, l))

    def Antecessor():
        l = '170 см'
        pl = 'в Европе'
        print("Homo Antecessor - человек предшествующий, живущий {0}, со средним ростом {1}".format(pl,l))

    def Floresiensis():
        l ='110 см'
        pl = 'в Индонезии'
        print("Homo Floresiensis -  гипотетический ископаемый карликовый вид людей, живущих {0}, со средним ростом {1}".format(pl,l))

    def Heidelbergensis():
        l = '140 см'
        pl = 'в Европе'
        print("Homo Heidelbergensis - европейская разновидность человека прямоходящего, живущего {0}, со средним ростом {1}".format(pl,l))

    def Neanderthalensis():
        l = '160 см'
        pl = 'в Европе и Средней Азии'
        print("Homo Neanderthalensis - вымерший или ассимилированный представитель рода людей, живущий {0}, со средним ростом {1}".format(pl, l))

    def Rhodesiensis():
        l  = '180 см'
        pl = 'в Замбии'
        print("Homo Rhodesiensis -  разновидности людей, чьи останки были обнаружены в пещере недалеко от города Брокен-Хилл в Северной Родезии, живущих {0}, со средним ростом {1}".format(pl, l))

    def Cepranensis():
        pl = 'в Италии'
        print("Homo Cepranensis - редлагаемое имя для вида трибы гоминини, описанного в 2003 году только по черепной крышке, живущих {0}".format(pl))

    def Georgicus():
        pl = 'в Грузии'
        print("Homo Georgicus -  вымершая форма гоминидов, чьи останки обнаружены на территории Грузии, живущих {0}".format(pl))

    def Naledi():
        pl = 'на юге Африке'
        print("Homo Naledi -  ископаемый вид людей трибы гоминини, живущих {0}".format(pl))

inp=input('Выберете\n1.Sapiens\n 2.Habilis\n3.Ergaster\n4.Erectus\n5.Antecessor\n6.Floresiensis\n7.Heidelbergensis\n8.Neanderthalensis\n9.Rhodesiensis\n10.Cepranensis\n11.Georgicus\n12.Naledi ')
inp=int(inp)
if inp<=6:
    if inp==5:
        Homo.Antecessor()
    if inp<=3:
        if inp<=2:
            if inp==1:
                Homo.Sapiens()
            else:
                Homo.Habilis()
        else:
            Homo.Ergaster()

    else:
        Homo.Erectus()

if inp<=9:
    if inp <=8:
        if inp==7:
            Homo.Heidelbergensis()
        else:
            Homo.Neanderthalensis()
    else:
        Homo.Rhodesiensis()

if inp<=11:
    if inp<=10:

        if inp==10:
            Homo.Cepranensis()
    else:
      Homo.Georgicus()
else:
    Homo.Naledi()
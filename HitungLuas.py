HitungLuas()

def HitungLuas():
    clearScreen()
    #MENU
    print("--PROGRAM HITUNG LUAS--")
    print("1.Persegi")
    print("2.Persegi Panjang")
    print("3.Segitiga")
    print("4.Lingkaran")
    print("0.Tutup")
    
    
    #Pilih Menu
    menu = input("pilih menu : ") #input nomor menu
    
    #Cek Menu Pilihan
    if menu==1:
        persegi()
    elif menu==2:
        persegipanjang()
    elif menu==3:
        segitga()
    elif menu==4:
        lingkaran()
    elif menu==0:
        clearScreen()
        print("Good Bye")
    else:
        print("Gak ada menunya gan")
        display_menu()
        
    def display_menu():
        #untuk menjeda program
        raw_input("")
        #Panggil fungsi HitungLuas()
        HitungLuas()
       
      
      def persegi():
      	clearScreen()
      print("--Luas Persegi :v--")
      
      sisi = input("Masukkan Panjang Sisi :")

      luas = sisi * sisi
      print "Luasnya Adalah",luas
      
      display_menu()
      
      def persegipanjang():
      	clearScreen()
      print("--Luas Persegi Panjang :v--")
      
      panjang = input("Masukkan Panjangnya :")
      lebar = input("Masukkan Lebarnya")
      
      luas = panjang * lebar
      print "Luasnya Adalah",luas
      
      display_menu()
      
      def segitiga():
      	clearScreen()
      print("--Luas Segitiga :v--")
      
      alas = input("Masukkan Nilai Alasnya :")
      tinggi = input("Masukkan Nilai Tingginya :")
      
      luas = alas * tinggi / 2
      print "Luasnya Adalah",luas
      
      display_menu()
      
      def lingkaran():
      	clearScreen()
      print("--Luas Lingkaran :v--")
      
      jari = input("Masukkan Jari-jarinya :")
      
      luas = jari * jari * 2 2 /  7
      
      display_menu()

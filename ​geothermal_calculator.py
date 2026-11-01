# Jeotermal Enerji Potansiyel Hesaplayıcı

debi = float(input("Su Akış Hızı (kg/s): "))
giris_sicakligi = float(input("Yeraltı Su Sıcaklığı (°C): "))
cikis_sicakligi = float(input("Tesisten Çıkış Sıcaklığı (°C): "))

# Su özgül ısısı (kJ/kg°C)
ozgul_isi = 4.184 
sicaklik_farki = giris_sicakligi - cikis_sicakligi
toplam_guc_kw = debi * ozgul_isi * sicaklik_farki

print(f"\nElde Edilen Termal Güç: {toplam_guc_kw:.2f} kW")

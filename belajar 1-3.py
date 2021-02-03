#latihan logika dan komparasi

#membuat nilai kurang 20 atau lebih dari 50

#+++++++++++++++20---------------50++++++++

masukkanNilai = float(input( "Masukkan nilai kurang dari 15\n atau\n lebih dari 10\n : "))

#++++++++20---------------------
isKurangDari = (masukkanNilai < 15)
print( "kurang dari 15 :", isKurangDari)

#-----------------50++++++++++++++
isLebihDari  = (masukkanNilai > 10)
print( "Lebih dari 10 :", isLebihDari)

jawabanbenar = isKurangDari or isLebihDari
print( "Jawaban nya adalah :", jawabanbenar)
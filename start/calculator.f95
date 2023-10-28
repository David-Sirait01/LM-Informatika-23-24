PROGRAM Calculator
  IMPLICIT NONE

  REAL :: a, b
  REAL, DIMENSION(4) :: var

  WRITE (*,*) 'Input 2 angka : '
  READ (*,*) a, b

  var(1) = a + b
  var(2) = a - b
  var(3) = a * b
  var(4) = a / b

  WRITE (*,*) 'Angka pertama  = ', a
  WRITE (*,*) 'Angka kedua    = ', b

  WRITE (*,*)
  WRITE (*,*) 'Penjumlahan -> ', var(1)
  WRITE (*,*) 'Pengurangan -> ', var(2)
  WRITE (*,*) 'Perkalian   -> ', var(3)
  WRITE (*,*) 'Pembagian   -> ', var(4)

  STOP
END PROGRAM Calculator

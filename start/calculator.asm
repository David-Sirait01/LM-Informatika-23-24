section .data
    prompt db "Input 2 angka : ", 0
    output_format db "Angka pertama = %f", 0
    output_format2 db "Angka kedua   = %f", 0
    output_format3 db "Penjumlahan -> %f", 0
    output_format4 db "Pengurangan -> %f", 0
    output_format5 db "Perkalian   -> %f", 0
    output_format6 db "Pembagian   -> %f", 0

section .bss
    a resq 1
    b resq 1

section .text
    global _start

_start:
    ; Input angka pertama
    mov rdi, 0
    mov rsi, prompt
    call printf
    mov rdi, a
    call scanf

    ; Input angka kedua
    mov rdi, 0
    mov rsi, prompt
    call printf
    mov rdi, b
    call scanf

    ; Hitung dan tampilkan hasil
    movq xmm0, [a]
    movq xmm1, [b]

    addsd xmm0, xmm1
    mov rsi, output_format3
    call printf

    subsd xmm0, xmm1
    mov rsi, output_format4
    call printf

    mulsd xmm0, xmm1
    mov rsi, output_format5
    call printf

    divsd xmm0, xmm1
    mov rsi, output_format6
    call printf

    ; Exit program
    mov rax, 60         ; syscall: exit
    xor rdi, rdi        ; status: 0
    syscall

section .data
    float_fmt db "%lf", 0

section .text
    global printf, scanf

printf:
    mov rax, 1
    mov rdi, 1
    mov rdx, 100
    syscall
    ret

scanf:
    mov rax, 0
    mov rdi, 0
    mov rdx, 100
    syscall
    ret

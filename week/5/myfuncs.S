section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rcx, rdx  ;move upper bound parameter & save it into counter reg rcx for looping
        
looper:
        mov [rdi], sil  ;write the first character @ starting address to val ([rdi] access element @ address rdi)
        add rdi, 1      ;move to the next index/character in memory
        loop looper     ;repeat this process until rcx is 0 (we've reached 'strl')
        
        
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        mov rcx, rdx  ;move upper bound parameter & save it into counter reg rcx for looping
        
looper2:
       mov bl, [rsi]  ;move current char in *src parameter into a temp reg
       mov [rdi], bl  ;move the current char in *src into the current spot in *dst
       add rsi, 1     ;increment the current position in *src
       add rdi, 1     ;increment the current position in *dst
       
       loop looper2   ;repeat this process until rcx is 0 (we've reached 'len')


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!

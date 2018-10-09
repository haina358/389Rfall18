Writeup 5 - Binaries I
======

Name: Hamid Aina
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Hamid Aina

## Assignment 5 Writeup

When I first began working on memset(), I began by creating pseudo code. I was able to model my solution with a mov call on a register, a loop, and another move call into a memory address. After revisiting the slides, I saw that the value for the counter register rcx is decremented after every iteration of a loop. From there, I knew I had to move the third parameter, strl, in register rdx into rcx. Within my loop I was able to retrieve the 2nd parameter of the function and write that into the current memory location of rdi by dereferencing it. I recalled how to do [rdi] from 216 and from there I just incremented the memory pointer of rdi. The loop would continue until rcx reaches 0 or equivalently, we’ve iterated ‘strl’ times.

Initially, I was unsure of how to move stack frames before and after a method call. But I saw that the starter code did that for us. For strncpy(), I followed mostly the same outline. I began by drafting my pseudo code approach and from there I began by moving the value in the third parameter into rcx again. After creating my loop label, I moved the current character in the *src parameter into a temporary register by dereferencing it and calling mov. I then called mov again to move that register’s value into the *dst parameter, [rdi]. After incrementing memory locations for rsi and rdi, my work for that iteration was done. Looping would terminate once rcx reaches 0 once again.

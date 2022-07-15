from tkinter import*
from PIL import Image,ImageTk
#importando pygame
import pygame
from pygame import mixer
import os

cor_cinza="#f0f3f5"
cor_branca="#feffff"
cor_verde="#3fb5a3"
cor_preta="#2e2d2c"
cor_azul="#4a88e8"


janela=Tk()
janela.title("")
janela.geometry("352x255")
janela.configure(background=cor_branca)
janela.resizable(width=False,height=False)



frame_esquerda=Frame(janela,width=150,height=150,bg=cor_preta)
frame_esquerda.grid(row=0,column=0,pady=1,padx=1,sticky=NSEW)

frame_direita=Frame(janela,width=250,height=150,bg=cor_preta)
frame_direita.grid(row=0,column=1,pady=1,padx=1,sticky=NSEW)

frame_baixo=Frame(janela,width=404,height=100,bg=cor_preta)
frame_baixo.grid(row=1,column=0,columnspan=3,pady=1,padx=0,sticky=NSEW)










#configurando frame esquerda
imagem_1=Image.open('img/icon1.png')
imagem_1=imagem_1.resize((130,130))
imagem_1=ImageTk.PhotoImage(imagem_1)

label_logo=Label(frame_esquerda,height=130,image=imagem_1,compound=LEFT,padx=0,anchor=NW,font=('Ivy 16 bold'),bg=cor_preta,fg=cor_preta)
label_logo.place(x=14,y=15)

#fucoes

def play_music():
    rodando=listbox.get(ACTIVE)
    label_rodando['text']=rodando
    mixer.music.load(rodando)
    mixer.music.play()
    
def pausar_music():
    mixer.music.pause()
    
def contiuar_music():
    mixer.music.unpause()
  
def parar_music():
    mixer.music.stop()
    
def proxima_music():
    tocando= label_rodando['text']
    index= musicas.index(tocando)
    
    novo_index=index+1
    tocando= musicas[novo_index]
    
    mixer.music.load(tocando)
    mixer.music.play()
    #deletando os elementos na playlist
    listbox.delete(0,END)
    
    mostrar()
    
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    label_rodando['text']= tocando
    
   
def anterior_music():
    tocando= label_rodando['text']
    index= musicas.index(tocando)
    
    novo_index=index -1
    tocando= musicas[novo_index]
    
    mixer.music.load(tocando)
    mixer.music.play()
    #deletando os elementos na playlist
    listbox.delete(0,END)
    
    mostrar()
    
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    label_rodando['text']= tocando
    
    
    
    
    
    
    
    
    

#configurando frame direita

lista=[]

listbox=Listbox(frame_direita,selectmode=SINGLE,font=('Arial 9 bold'),width=22,height=10,bg=cor_preta,fg=cor_branca)
listbox.grid(row=0,column=0)

s = Scrollbar(frame_direita)
s.grid(row=0,column=1,sticky=NSEW)


listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

    

#configurando frame baixo

label_rodando=Label(frame_baixo,text='escolha música na lista',width=44,justify=LEFT,anchor=NW,font=('Ivy 10'),bg=cor_branca,fg=cor_preta)
label_rodando.place(x=0,y=1)


#botoes


imagem_2=Image.open('img/2.png')
imagem_2=imagem_2.resize((30,30))
imagem_2=ImageTk.PhotoImage(imagem_2)

butao_anterior=Button(frame_baixo,width=40,command=anterior_music,image=imagem_2,relief=RAISED,overrelief=RIDGE,height=40,font=('Ivy 10 bold'),bg=cor_preta,fg=cor_branca)
butao_anterior.place(x=38,y=35)

imagem_3=Image.open('img/3.png')
imagem_3=imagem_3.resize((30,30))
imagem_3=ImageTk.PhotoImage(imagem_3)

butao_play=Button(frame_baixo,command=play_music,width=40,image=imagem_3,relief=RAISED,overrelief=RIDGE,height=40,font=('Ivy 10 bold'),bg=cor_preta,fg=cor_branca)
butao_play.place(x=84,y=35)

imagem_4=Image.open('img/4.png')
imagem_4=imagem_4.resize((30,30))
imagem_4=ImageTk.PhotoImage(imagem_4)

butao_proxima=Button(frame_baixo,command=proxima_music,width=40,image=imagem_4,relief=RAISED,overrelief=RIDGE,height=40,font=('Ivy 10 bold'),bg=cor_preta,fg=cor_branca)
butao_proxima.place(x=130,y=35)

imagem_5=Image.open('img/5.png')
imagem_5=imagem_5.resize((30,30))
imagem_5=ImageTk.PhotoImage(imagem_5)

butao_pausar=Button(frame_baixo,command=pausar_music,width=40,image=imagem_5,relief=RAISED,overrelief=RIDGE,height=40,font=('Ivy 10 bold'),bg=cor_preta,fg=cor_branca)
butao_pausar.place(x=176,y=35)

imagem_6=Image.open('img/6.png')
imagem_6=imagem_6.resize((30,30))
imagem_6=ImageTk.PhotoImage(imagem_6)

butao_continuar=Button(frame_baixo,command=contiuar_music,width=40,image=imagem_6,relief=RAISED,overrelief=RIDGE,height=40,font=('Ivy 10 bold'),bg=cor_preta,fg=cor_branca)
butao_continuar.place(x=222,y=35)

imagem_7=Image.open('img/7.png')
imagem_7=imagem_7.resize((30,30))
imagem_7=ImageTk.PhotoImage(imagem_7)

butao_stop=Button(frame_baixo,command=parar_music,width=40,image=imagem_7,relief=RAISED,overrelief=RIDGE,height=40,font=('Ivy 10 bold'),bg=cor_preta,fg=cor_branca)
butao_stop.place(x=268,y=35)


os.chdir(r'C:\Users\tiyas\Documents\Dev\Estudos Python\playmusic\music')
musicas=os.listdir()

def  mostrar():
   for i in musicas:
     listbox.insert(END,i)
     
     
     
     
     
     
mostrar()     
     

    


#inicializando o mixer
mixer.init()

janela.mainloop()
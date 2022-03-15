from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap('fold.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/img5.jpg"))

# lista das imagens
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


# Definindo a Exibição das imagens na tela
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

# Função resposavel por fazer o botão avançar funcionar
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() #serve para "apagar" a imagem para dar lugar a proxima
    my_label = Label(image=image_list[image_number-1])# como  a lista é lida a apertir de "0" é preciso subtrair -1 no inicio do programa 
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))# toda vez que o botão é pressionado é adicionado o valor de 1 para saltar para a proxima imagem.
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))#para ultilizar o botão voltar, ele ira subtrair -1  para voltar atras.
    
    # Bem Intuitivo, não?
    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    
def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
        
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# Definição dos botões
button_back = Button(root, text="<<", command=DISABLED)
button_quit = Button(root, text="QUIT", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# Posições dos Botões
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()


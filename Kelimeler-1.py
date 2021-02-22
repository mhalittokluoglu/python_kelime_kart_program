import tkinter as tk

class MyProgram:
    def __init__(self,win):

        with open('Kelimeler-1.txt','r',encoding='UTF-8') as f:
            words = []
            for line in f:
                words.append(line)

        self.counter = 0
        self.words_1 = []
        self.words_2 = []
        self.counter2 = -1
        for item in words:
            splitted_words = item.split('=')
            self.words_1.append(splitted_words[0])
            self.words_2.append(splitted_words[1])
            self.counter2 += 1

        main_frame = tk.Frame(win)
        self.label_1 = tk.Label(main_frame,text = self.words_1[self.counter],width = 30,font = 'Times 32 bold',height = 3)
        self.label_2 = tk.Label(main_frame,text = '',width = 50,font = 'Times 25',height = 3)
        self.next_button = tk.Button(main_frame,text = 'Sonraki',font = 'Times 17', command = self.next_func)
        self.prev_button = tk.Button(main_frame,text = 'Önceki',font = 'Times 17', command = self.prev_func)
        self.show_button = tk.Button(main_frame,text = 'Göster',font = 'Times 17', command = self.show_words2)

        main_frame.pack()
        self.label_1.grid(row = 0, column = 0, columnspan = 3)
        self.label_2.grid(row = 1, column = 0, columnspan = 3)
        self.prev_button.grid(row = 2, column = 0)
        self.show_button.grid(row = 2, column = 1)
        self.next_button.grid(row = 2, column = 2)


    def show_words2(self):
        self.label_1['text'] = self.words_1[self.counter]
        self.label_2['text'] = self.words_2[self.counter]

    def next_func(self):
        if self.counter < self.counter2:
            self.counter += 1
            self.label_1['text'] = self.words_1[self.counter]
            self.label_2['text'] = ''


    def prev_func(self):
        if self.counter > 0:
            self.counter -= 1
            self.label_1['text'] = self.words_1[self.counter]
            self.label_2['text'] = ''

win = tk.Tk()
win.title('Kelime Kartı Python Programı')
prog = MyProgram(win)
win.mainloop()

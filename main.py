# Copyright (c) 2020 SilverGem silverjunk08@gmail.com
# All rights reserved.
# Licensed under the LGPL. See LICENSE file for full license information.


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock 
from kivy.properties import Property
import random


class MyApp(App):
	def build(self):
		self.layout = GridLayout(rows=50, cols=2)

		file = open("Kanji_List.txt","r",encoding="utf8")
		txt = file.readline()
		file.close()
		txt = txt.split("@@")
		for num, c in enumerate(txt):
			txt[num] = c.split(",")
			for num2, d in enumerate(txt[num]):
				txt[num][num2] = txt[num][num2].replace("!", " ")
		dic = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[]}
		for c in txt:
			if c[1] == "S":
				c[1] = "7"
			dic[c[1]].append(c)
		for c in dic:
			for num, d in enumerate(dic[c]):
				del dic[c][num][1]

		self.dic = dic
		self.check_lst = [0,0,0,0,0,0,0]
		self.cardcount = 10

		MyApp.menu(self)

		return self.layout

	def cardcountdecbtn(self, *argv):
		if self.cardcount != 2:
			self.cardcount -= 1
		self.lblboxcrdcnt.text = "Card Count {crdcnt}".format(crdcnt=self.cardcount)

	def cardcountincbtn(self, *argv):
		if self.cardcount != 80:
			self.cardcount += 1
		self.lblboxcrdcnt.text = "Card Count {crdcnt}".format(crdcnt=self.cardcount)

	def menu(self):
		self.check_lst = [0,0,0,0,0,0,0]

		cardcountdecbtn = Button(text="-")
		cardcountdecbtn.bind(on_press=self.cardcountdecbtn)
		self.layout.add_widget(cardcountdecbtn)

		self.lblboxcrdcnt = Label(text="Card Count {crdcnt}".format(crdcnt=self.cardcount))
		self.layout.add_widget(self.lblboxcrdcnt)

		cardcountincbtn = Button(text="+")
		cardcountincbtn.bind(on_press=self.cardcountincbtn)
		self.layout.add_widget(cardcountincbtn)

		lblbox1 = Label(text="")
		self.layout.add_widget(lblbox1)

		chkbx1 = CheckBox()
		chkbx1.bind(active=self.chkbx1)
		self.layout.add_widget(chkbx1)

		lblbox1 = Label(text="Level 1")
		self.layout.add_widget(lblbox1)

		chkbx2 = CheckBox()
		chkbx2.bind(active=self.chkbx2)
		self.layout.add_widget(chkbx2)

		lblbox2 = Label(text="Level 2")
		self.layout.add_widget(lblbox2)

		chkbx3 = CheckBox()
		chkbx3.bind(active=self.chkbx3)
		self.layout.add_widget(chkbx3)

		lblbox3 = Label(text="Level 3")
		self.layout.add_widget(lblbox3)

		chkbx4 = CheckBox()
		chkbx4.bind(active=self.chkbx4)
		self.layout.add_widget(chkbx4)

		lblbox4 = Label(text="Level 4")
		self.layout.add_widget(lblbox4)

		chkbx5 = CheckBox()
		chkbx5.bind(active=self.chkbx5)
		self.layout.add_widget(chkbx5)

		lblbox5 = Label(text="Level 5")
		self.layout.add_widget(lblbox5)

		chkbx6 = CheckBox()
		chkbx6.bind(active=self.chkbx6)
		self.layout.add_widget(chkbx6)

		lblbox6 = Label(text="Level 6")
		self.layout.add_widget(lblbox6)

		chkbx7 = CheckBox()
		chkbx7.bind(active=self.chkbx7)
		self.layout.add_widget(chkbx7)

		lblbox7 = Label(text="Level 7")
		self.layout.add_widget(lblbox7)

		autobtn = Button(text="Auto")
		autobtn.bind(on_press=self.autobtn)
		self.layout.add_widget(autobtn)

		cardsbtn = Button(text="Cards")
		cardsbtn.bind(on_press=self.cardsbtn)
		self.layout.add_widget(cardsbtn)

	def chkbx1(self, *argv):
		if argv[1]:
			self.check_lst[0] = 1
		else:
			self.check_lst[0] = 0

	def chkbx2(self, *argv):
		if argv[1]:
			self.check_lst[1] = 1
		else:
			self.check_lst[1] = 0

	def chkbx3(self, *argv):
		if argv[1]:
			self.check_lst[2] = 1
		else:
			self.check_lst[2] = 0

	def chkbx4(self, *argv):
		if argv[1]:
			self.check_lst[3] = 1
		else:
			self.check_lst[3] = 0

	def chkbx5(self, *argv):
		if argv[1]:
			self.check_lst[4] = 1
		else:
			self.check_lst[4] = 0

	def chkbx6(self, *argv):
		if argv[1]:
			self.check_lst[5] = 1
		else:
			self.check_lst[5] = 0

	def chkbx7(self, *argv):
		if argv[1]:
			self.check_lst[6] = 1
		else:
			self.check_lst[6] = 0


	def exitautobtn(self, *argv):
		Clock.unschedule(self.auto_choose)
		self.layout.clear_widgets()
		MyApp.menu(self)

	def auto_choose(self, *argv):
		chosen = random.choice(self.lst_to_use)

		self.chosenkanji.text = chosen[0]
		self.chosenkanjipro.text = chosen[1]
		self.chosenkanjimeaning.text = chosen[2]


	def autobtn(self,*argv):
		if 1 in self.check_lst:
			self.layout.clear_widgets()
			lst_to_use = []
			for num, c in enumerate(self.check_lst):
				if c == 1:
					lst_to_use += self.dic[str(num+1)]
			self.lst_to_use = lst_to_use

			chosen = random.choice(self.lst_to_use)

			exitautobtn = Button(text="Menu",size_hint=(.35,.2))
			exitautobtn.bind(on_press=self.exitautobtn)
			self.layout.add_widget(exitautobtn)

			padding = Label(text="",size=(0,0),size_hint=(None,None))
			self.layout.add_widget(padding)

			self.chosenkanji = Label(text=chosen[0],font_size=300,font_name="NotoSansJP.otf",size_hint=(1,.2))
			self.layout.add_widget(self.chosenkanji)

			padding = Label(text="",size=(0,0),size_hint=(None,None))
			self.layout.add_widget(padding)

			# self.chosenkanjipro = Label(text=chosen[1],font_size=30,font_name="NotoSansJP.otf",size_hint=(1,.2))
			# self.layout.add_widget(self.chosenkanjipro)

			self.chosenkanjipro = Label(text=chosen[1], font_size=30, font_name="NotoSansJP.otf", size_hint=(1,.2))
			self.chosenkanjipro.bind(width=lambda *x: self.chosenkanjipro.setter('text_size')(self.chosenkanjipro,(self.chosenkanjipro.width, None)), texture_size=lambda *x: self.chosenkanjipro.setter('height')(self.chosenkanjipro,self.chosenkanjipro.texture_size[1]))
			self.layout.add_widget(self.chosenkanjipro)

			padding = Label(text="",size=(0,0),size_hint=(None,None))
			self.layout.add_widget(padding)

			self.chosenkanjimeaning = Label(text=chosen[2],font_size=75,font_name="NotoSansJP.otf",size_hint=(1,.2))
			self.layout.add_widget(self.chosenkanjimeaning)

			Clock.schedule_interval(self.auto_choose, 7)


	def exitcardsbtn(self, *argv):
		self.layout.clear_widgets()
		MyApp.menu(self)

	def checkbtn(self, *argv):
		if argv[0].text == self.correct[2]:
			self.twicechk += 1
			if self.twicechk >= 2:
				MyApp.cards_choose(self)
			argv[0].background_color = (0,1,0,1)
		else:
			argv[0].background_color = (1,0,0,1)

	def cards_choose(self, *argv):
		self.layout.clear_widgets()

		self.twicechk = 0

		using_lst = []
		using_lst = random.sample(self.lst_to_use, k=self.cardcount)
		self.correct = random.choice(using_lst)

		exitcardsbtn = Button(text="Menu",size_hint=(.35,.2))
		exitcardsbtn.bind(on_press=self.exitcardsbtn)
		self.layout.add_widget(exitcardsbtn)

		padding = Label(text="",size=(0,0),size_hint=(None,None))
		self.layout.add_widget(padding)

		chosenkanji = Label(text=self.correct[0],font_size=125,font_name="NotoSansJP.otf",size_hint=(1,.2))
		self.layout.add_widget(chosenkanji)

		padding = Label(text="",size=(0,0),size_hint=(None,None))
		self.layout.add_widget(padding)

		# chosenkanjipro = Label(text=self.correct[1],font_size=20,font_name="NotoSansJP.otf",size_hint=(1,.2))
		# self.layout.add_widget(chosenkanjipro)

		chosenkanjipro = Label(text=self.correct[1], font_size=20, font_name="NotoSansJP.otf", size_hint=(1,.2))
		chosenkanjipro.bind(width=lambda *x: chosenkanjipro.setter('text_size')(chosenkanjipro,(chosenkanjipro.width, None)), texture_size=lambda *x: chosenkanjipro.setter('height')(chosenkanjipro,chosenkanjipro.texture_size[1]))
		self.layout.add_widget(chosenkanjipro)

		padding = Label(text="",size=(0,0),size_hint=(None,None))
		self.layout.add_widget(padding)

		for c in range(self.cardcount):
			chsbtn = Button(text=using_lst[c][2],background_color=(1,1,1,1),size_hint=(1,.2)) 
			chsbtn.bind(on_press=self.checkbtn)
			self.layout.add_widget(chsbtn)


	def cardsbtn(self,*argv):
		if 1 in self.check_lst:
			self.layout.clear_widgets()

			lst_to_use = []
			for num, c in enumerate(self.check_lst):
				if c == 1:
					lst_to_use += self.dic[str(num+1)]
			self.lst_to_use = lst_to_use

			MyApp.cards_choose(self)




MyApp().run()
import simpleaudio as sa
import time
import sys

def main():

	text = input("Veuillez entrer la phrase a traduire en morse : ")
	longueur = len(text)
	print(" ")
	nb = -1

	wave_obj = sa.WaveObject.from_wave_file("point.wav")
	wave_obj1 = sa.WaveObject.from_wave_file("trait.wav")


	a = ".- "
	b = "-... "
	c = "-.-. "
	d = "-.. "
	e = ". "
	f =	"..-. "
	g = "--. "
	h = ".... "
	i = ".. "
	j = ".--- "
	k = "-.- "
	l = ".-.. "
	m = "-- "
	n = "-. "
	o = "--- "
	p = ".--. "
	q = "--.- "
	r = ".-. "
	s = "... "
	t = "- "
	u = "..- "
	v = "...- "
	w = ".-- "
	x = "-..- "
	y = "-.-- "
	z = "--.. "

	for i in range(longueur):
		nb = nb + 1

		if text[nb] == "a":
			test = "test"
			time.sleep(0.5)
			#print(test,end ='')
			print(a[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(a[1],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()


		if text[nb] == "b":
			time.sleep(0.5)
			print(b[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(b[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(b[2],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(b[3],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "c":
			time.sleep(0.5)
			print(c[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(c[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(c[2],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(c[3],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "d":
			time.sleep(0.5)
			print(d[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(d[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(d[2],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "e":
			time.sleep(0.5)
			print(e[0],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "f":
			time.sleep(0.5)
			print(f[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(f[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(f[2],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(f[3],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "g":
			time.sleep(0.5)
			print(g[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(g[1],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(g[2],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "h":
			time.sleep(0.5)
			print(h[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(h[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(h[2],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(h[3],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "i":
			time.sleep(0.5)
			print(i[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(i[1],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "j":
			time.sleep(0.5)
			print(j[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(j[1],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(j[2],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(j[3],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "k":
			time.sleep(0.5)
			print(k[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(k[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(k[2],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "l":
			time.sleep(0.5)
			print(l[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(l[1],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(l[2],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(l[3],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "m":
			time.sleep(0.5)
			print(m[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(m[1],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "n":
			time.sleep(0.5)
			print(n[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(n[1],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "o":
			time.sleep(0.5)
			print(o[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(o[1],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(o[2],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "p":
			time.sleep(0.5)
			print(p[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(p[1],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(p[2],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(p[3],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "q":
			time.sleep(0.5)
			print(q[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(q[1],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(q[2],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(q[3],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "r":
			time.sleep(0.5)
			print(r[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(r[1],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(r[2],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "s":
			time.sleep(0.5)
			print(s[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(s[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(s[2],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == "t":
			time.sleep(0.5)
			print(t[0],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "u":
			time.sleep(0.5)
			print(u[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(u[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(u[2],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "v":
			time.sleep(0.5)
			print(v[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(v[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(v[2],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(v[3],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "w":
			time.sleep(0.5)
			print(w[0],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(w[1],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(w[2],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "x":
			time.sleep(0.5)
			print(x[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(x[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(x[2],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(x[3],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "y":
			time.sleep(0.5)
			print(y[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(y[1],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(y[2],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(y[3],end=" ",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()

		if text[nb] == "z":
			time.sleep(0.5)
			print(z[0],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(z[1],end="",flush=True)
			play_obj1 = wave_obj1.play()
			play_obj1.wait_done()
			time.sleep(0.1)
			print(z[2],end="",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.1)
			print(z[3],end=" ",flush=True)
			play_obj = wave_obj.play()
			play_obj.wait_done()

		if text[nb] == " ":
			print("  ")

		#else:
			#sys.exit()




if __name__ == "__main__":
    main()

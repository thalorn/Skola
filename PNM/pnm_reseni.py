import numpy as np
import math

a = 3       # a > 0
alpha = 1   # promenna y(0) = alpha
beta = 0    # promenna y'(0) = beta
gamma = 1   # promenna y'(1) = gamma
tolerance = 1.0e-7

# guess range
g_min = -13 
g_max =  13

def soubor(x, y1, y2, y3, filename):
    file = open(filename, 'w')
    file.write("#x\ty\n")
    for i in range(len(x)):
        file.write(str(x[i]) + '\t' + str(y1[i]) + '\n')
    file.close()
    print("Soubor vygenerován.")
 
def f1(x, y1, y2, y3):
    return (-3*a*x*y3 - 3*a*a*x*x*y2 - a*a*a*x*x*x*y1)
    
def f2(x, y1, y2, y3):
    return y3
    
def f3(x, y1, y2, y3):
    return y2

def rk4(x0, x1, y1_0, y2_0, y3_0, n):
    vx = [0] * (n + 1)
    vy1 = [0] * (n + 1)
    vy2 = [0] * (n + 1)
    vy3 = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy1[0] = y1 = y1_0
    vy2[0] = y2 = y2_0
    vy3[0] = y3 = y3_0
    for i in range(1, n + 1):
        k1 = h * f1(x, y1, y2, y3)
        l1 = h * f2(x, y1, y2, y3)
        m1 = h * f3(x, y1, y2, y3)
        
        k2 = h * f1(x + 0.5 * h, y1 + 0.5 * k1, y2 + 0.5 * l1, y3 + 0.5 * m1)
        l2 = h * f2(x + 0.5 * h, y1 + 0.5 * k1, y2 + 0.5 * l1, y3 + 0.5 * m1)
        m2 = h * f3(x + 0.5 * h, y1 + 0.5 * k1, y2 + 0.5 * l1, y3 + 0.5 * m1)
        
        k3 = h * f1(x + 0.5 * h, y1 + 0.5 * k2, y2 + 0.5 * l2, y3 + 0.5 * m2)
        l3 = h * f2(x + 0.5 * h, y1 + 0.5 * k2, y2 + 0.5 * l2, y3 + 0.5 * m2)
        m3 = h * f3(x + 0.5 * h, y1 + 0.5 * k2, y2 + 0.5 * l2, y3 + 0.5 * m2)
        
        k4 = h * f1(x + h, y1 + k3, y2 + l3, y3 + m3)
        l4 = h * f2(x + h, y1 + k3, y2 + l3, y3 + m3)
        m4 = h * f3(x + h, y1 + k3, y2 + l3, y3 + m3)
        
        vx[i] = x = x0 + i * h
        
        vy1[i] = y1 = y1 + (k1 + k2 + k2 + k3 + k3 + k4) / 6
        vy2[i] = y2 = y2 + (l1 + l2 + l2 + l3 + l3 + l4) / 6
        vy3[i] = y3 = y3 + (m1 + m2 + m2 + m3 + m3 + m4) / 6
    return vx, vy1, vy2, vy3

def strelba(alpha, beta, gamma, g_min,g_max):
    i = 0 #pocet iteraci
    vox, vy1_1, vy2_1, vy3_o = rk4(0, 1, alpha, beta, g_min, 100)
    vox, vy1_2, vy2_2, vy3_p = rk4(0, 1, alpha, beta, g_max, 100)
    mini = vy2_1[-1] - gamma
    #print(mini)
    maxi = vy2_2[-1] - gamma
    #print(maxi)
    if maxi*mini > 0:
        print("interval je vedle")
    # zaciname zleva
    odchylka = mini
    while abs(odchylka) > tolerance:
        #pulka intervalu
        y_mid = (g_min + g_max)/2
        #rk4 pustim se stredem intervalu, zajímá me zda se blizim k vy2 neboli y'(1) = gamma
        vox, vy1, vy2, vy3 = rk4(0, 1, alpha, beta, y_mid, 100)
        #rozdil noveho vysledku - odchylka
        odchylka = vy2[-1] - gamma
        # volím nové hranice intervalù
        if (mini > 0 and odchylka < 0) or (mini < 0 and odchylka > 0):
            g_max = y_mid
            maxi = odchylka
        elif (odchylka > 0 and maxi < 0) or (odchylka < 0 and maxi > 0):
            g_min = y_mid
            mini = odchylka
    return vox, vy1, vy2, vy3


#------------MAIN-------------#
# pustim strelbu
print("Řeším příklad y``` + 3axy`` + 3a^2x^2y` + a^3x^3y, kde x (0,1), a > 0\n")
print("Počáteční podmínky:\n y(0)=" + str(alpha) +", y`(0)=" + str(beta) +", y`(1)= " + str(gamma) + "\n")
print("Parametr a = " + str(a))

print("Rovnici BVP jsem rozložil na soustavu tří rovnic IVP:")
print("y1` =                         y2")
print("y2` =                                     y3")
print("y3` = -a^3 x^3 y1 - 3 a^2 x^2 y2 - -3 a x y3")

print("A řeším pomocí RK4 pro soustavu tří rovnic.")
vox, vy1, vy2, vy3 = strelba(alpha, beta, gamma, g_min, g_max)
print("Používám maximální odchylku (toleranci): " + str(tolerance) + "\n")
#vysledek vypisu do souboru
soubor(vox, vy1, vy2, vy3, 'data.txt')
